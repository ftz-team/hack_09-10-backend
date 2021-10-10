from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import tree

from .helpers import get_analytics
from .managers import UserManager

BASE_URL = 'http://194.67.108.25:7000'
# BASE_URL = 'http://127.0.0.1:8000'

@receiver(post_save, sender='core.Dataset')
def update_dataset_metadata(sender, instance=None, created=False, **kwargs):
    if created:
        path = BASE_URL + instance.data.url
        print(path)
        json_metadata = get_analytics(path_to_file=path)
        instance.analytics = json_metadata
        instance.save()


class Tag(models.Model):
    name = models.CharField(max_length=1000)


class Role(models.Model):
    name = models.CharField(max_length=1000)
    company = models.ForeignKey('core.Company', on_delete=models.CASCADE, default=1, blank=True, null=True)
    datasets = models.ManyToManyField('core.Dataset', related_name='role_datasets', blank=True)


class Application(models.Model):
    status = models.IntegerField()
    json = models.FileField()
    user = models.ForeignKey('core.User', on_delete=models.CASCADE, default=1, blank=True, null=True)
    price = models.IntegerField()


class Task(models.Model):
    status = models.IntegerField()
    new_dataset = models.ForeignKey('core.Dataset', on_delete=models.CASCADE, default=1, blank=True, null=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, default=1, blank=True, null=True)


class Dataset(models.Model):
    name = models.CharField(max_length=1000)
    tags = models.ManyToManyField(Tag, related_name='dataset_tags', blank=True)
    STATUS_CHOICES = [
        (0, 'В обработке'),
        (1, 'Готов'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES, blank=True, null=True)
    TYPE_CHOICES = [
        (0, 'Приватный'),
        (1, 'Публичный')
    ]
    type = models.IntegerField(choices=TYPE_CHOICES, blank=True, null=True)
    analytics = models.JSONField(blank=True, null=True, default=dict)
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    owner = models.ForeignKey('core.Company', on_delete=models.CASCADE, default=1, blank=True, null=True)
    description = models.CharField(max_length=1000, default='', blank=True, null=True)
    price_per_row = models.IntegerField(default=1, blank=True, null=True)
    price_per_feature = models.IntegerField(default=1, blank=True, null=True)
    data = models.FileField(blank=True, null=True) 


class Company(models.Model):
    name = models.CharField(max_length=1000)
    logo = models.ImageField()
    admin = models.ForeignKey('core.User', related_name='company_admin', on_delete=models.CASCADE, default=1, blank=True, null=True)
    datasets = models.ManyToManyField(Dataset, related_name='company_datasets', blank=True)
    balance = models.IntegerField()


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=1000, default='', blank=True, null=True)
    last_name = models.CharField(max_length=1000, default='', blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    roles = models.ManyToManyField('core.Role', related_name='user_roles', blank=True)
    available_datasets = models.ManyToManyField(Dataset, related_name='user_available_datasets', blank=True)

    # system
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.first_name + self.last_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_superuser