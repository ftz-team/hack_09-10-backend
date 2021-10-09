from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from .managers import UserManager


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
    status = models.IntegerField()
    analytics = models.FileField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    owner = models.ForeignKey('core.Company', on_delete=models.CASCADE, default=1, blank=True, null=True)
    description = models.CharField(max_length=1000, default='')
    price_per_row = models.IntegerField(default=1)
    price_per_feature = models.IntegerField(default=1)
    data = models.FileField() 


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