# -*- coding: utf-8 -*-
# vim:tabstop=4:shiftwidth=4:expandtab

# import os
from joblib import load
import numpy as np

from django.conf import settings

clf = load(settings.IRIS_SAVE_FILE)

def get_model():
    return clf


def predict(data):
    # X = np.array([data['sepal_length'], data['sepal_width'],
    #               data['petal_length'], data['petal_width']]).reshape(1, -1)
    # assert len()
    X = np.array(
        [data[col] for col in settings.IRIS_DATA_COLUMN_LIST]
    ).reshape(1, -1)
    pred_one_hot = clf.predict(X)
    pred_label = np.argmax(np.squeeze(pred_one_hot), axis=0)
    return settings.IRIS_NAME_LIST[pred_label]
