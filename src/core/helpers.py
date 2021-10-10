import pandas as pd 
import numpy as np
import json

def get_analytics(path_to_file):
    print(path_to_file)
    df = pd.read_csv(path_to_file)

    res = {}

    res['features'] = {}

    features_df = []

    null_df = df.isnull()

    for feature in df:
        #features_df.append(str(feature))
        dsc = df[feature].describe()
        res['features'][feature] = dsc.to_dict()
        type = "numeric"
        if ( str(dsc.dtype) == "object"):
            type = "categorical"
        res['features'][feature]['type'] = type
        res['features'][feature]['memory_usage'] = df[feature].memory_usage()
        res['features'][feature]['missing_values'] = sum(null_df[feature])
        if type == "categorical":
            most_common_names = df[feature].value_counts()[:10].index.tolist()
            most_common_values = [df[feature].value_counts()[i] for i in df[feature].value_counts()[:10].index.tolist()]
            res['features'][feature]['graphics'] = {
                'most_common' : {
                    'labels' : most_common_names,
                    'values' : most_common_values
                }
            }
        else:
            pass
            


    res['insights'] = {
        'rows_count' : len(df),
        'memory_usage' : df.memory_usage(index=True).sum(),
        'missing_rows' : len(df[df.isna().any(axis=1)]),
        'duplicated_rows' : len(df.duplicated()),
        'duplicated_rows_percents' : len(df.duplicated()) / len(df),
        'correlations' : df.corr(method ='pearson').to_dict("records"),
        'correlations_names' :  df.corr(method ='pearson').to_dict("split")['index'],
        'features_df' : df.columns.values.tolist(),
        'head' : df.head(5).fillna("Nan").to_dict("records")
    }

    class NumpyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            elif isinstance(obj, np.int64):
                return int(obj)
            return json.JSONEncoder.default(self, obj)

    json_dump = json.dumps(res, cls=NumpyEncoder)
    return json_dump
