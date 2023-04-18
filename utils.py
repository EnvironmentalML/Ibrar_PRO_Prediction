#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    utils.py
# @Author:      Kuro
# @Time:        18/4/2023 3:25 AM

import pickle


def load_model(model_power, model_aw, model_b, model_s):
    return [pickle.load(open(model_power, 'rb')), pickle.load(open(model_aw, 'rb')),
            pickle.load(open(model_b, 'rb')), pickle.load(open(model_s, 'rb'))]


def encode_data(df, encode_col, encode_path):
    le = pickle.load(open(encode_path, 'rb'))
    df[encode_col] = le.fit_transform(df[encode_col])
    return df


def scale_data(X_test, scale_path):
    scaler = pickle.load(open(scale_path, 'rb'))
    X_test = scaler.transform(X_test)

    return X_test
