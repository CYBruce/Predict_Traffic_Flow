"""
Processing the data
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def process_data(train, test, lags):
    """Process data
    Reshape and split train\test data.

    # Arguments
        train: String, name of .csv train file.
        test: String, name of .csv test file.
        lags: integer, time lag.
    # Returns
        X_train: ndarray.
        y_train: ndarray.
        X_test: ndarray.
        y_test: ndarray.
        scaler: StandardScaler.
    """
    attr = ['Lane 1 Flow (Veh/5 Minutes)','Occ','Speed']
    attr_num = len(attr)
    df1 = pd.read_csv(train, encoding='utf-8').fillna(0)
    df2 = pd.read_csv(test, encoding='utf-8').fillna(0)
    
    scaler = StandardScaler().fit(df1[attr].values)
    scaler = MinMaxScaler(feature_range=(0, 1)).fit(df1[attr].values.reshape(-1, attr_num))
    Min = min(df1[attr[0]])#the minimum flow
    Max = max(df1[attr[0]])#the maximum flow
    flow1 = scaler.transform(df1[attr].values.reshape(-1, attr_num)).reshape(1, -1)[0]
    flow2 = scaler.transform(df2[attr].values.reshape(-1, attr_num)).reshape(1, -1)[0]
    train, test = [], []
    for i in range(lags, int(len(flow1)/attr_num)):
        train.append(flow1[attr_num*(i - lags): attr_num*i + 1])
    for i in range(lags, int(len(flow2)/attr_num)):
        test.append(flow2[attr_num*(i - lags): attr_num*i + 1])

    train = np.array(train)
    test = np.array(test)

    np.random.shuffle(train)

    X_train = train[:, :-1]
    y_train = train[:, -1]
    X_test = test[:, :-1]
    y_test = test[:, -1]

    return X_train, y_train, X_test, y_test, scaler, Min, Max
