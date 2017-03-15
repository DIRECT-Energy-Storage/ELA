"""Functions for exploring and evaluating a K-nearest-neighbors model
with different parameters and data sets"""

import ela
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

gen = ela.gen_data
stor = ela.stor_data


def count_types(df):
    """
    Print a list of energy types and number of facilities of each type.

    Parameters
    ----------
    df : Pandas dataframe
        Must contain a 'type' column.

    """

    for tp in df.type.unique():
        print(tp, len(df[df.type == tp]))


def predict_types(k, weights, train_df, test_df):
    """
    Fit KNN model and record predicted energy types for training/testing data.

    Parameters
    ----------
    k : int
        Number of nearest-neighbors to consider in KNN model.
    weights : string
        Type of weighting to use for KNN model ('distance' or 'uniform')
    train_df : Pandas dataframe
        Data to use for training the KNN model.
        X coordinates are the 'lat' and 'lon' columns.
        Y values (predicted types) are the 'type' column.
    test_df : Pandas dataframe
        Data to use for test the KNN model.
        X coordinates are the 'lat' and 'lon' columns.
        Y values (predicted types) are the 'type' column.


    Side Effects
    ------------
    Adds 'pred' column to both train_df and test_df, containing predicted
    energy type for each location.

    """

    clf = KNeighborsClassifier(n_neighbors=k, weights=weights)
    clf.fit(train_df[['lat', 'lon']], np.ravel(train_df.type))
    train_df.loc[:, 'pred'] = clf.predict(train_df[['lat', 'lon']])
    test_df.loc[:, 'pred'] = clf.predict(test_df[['lat', 'lon']])


def count_pred_types(df):
    """
    Print a list of predicted energy types and number of facilities of each type.

    Parameters
    ----------
    df : Pandas dataframe
        Must contain a 'pred' column.

    """

    for tp in df.pred.unique():
        print(tp, len(df[df.pred == tp]))


def try_k(k, weights, train_df, test_df):
    """
    Fit KNN model and return training and testing error.

    Parameters
    ----------
    k : int
        Number of nearest-neighbors to consider in KNN model.
    weights : string
        Type of weighting to use for KNN model ('distance' or 'uniform')
    train_df : Pandas dataframe
        Data to use for training the KNN model.
        X coordinates are the 'lat' and 'lon' columns.
        Y values (predicted types) are the 'type' column.
    test_df : Pandas dataframe
        Data to use for test the KNN model.
        X coordinates are the 'lat' and 'lon' columns.
        Y values (predicted types) are the 'type' column.


    Return
    ------
    (train_error, test_error) : tuple of floats
        Training error rate and testing error rate for the KNN model.

    """

    clf = KNeighborsClassifier(n_neighbors=k, weights=weights)
    x_train = train_df[['lat', 'lon']]
    y_train = np.ravel(train_df.type)
    clf.fit(x_train, y_train)
    x_test = test_df[['lat', 'lon']]
    y_test = np.ravel(test_df.type)

    train_error = 1 - clf.score(x_train, y_train)
    test_error = 1 - clf.score(x_test, y_test)
    return train_error, test_error


def try_k_range(k_list, weights, train_df, test_df):
    """
    Evaluate KNN model and return training and testing error for different K.

    Parameters
    ----------
    k_list : list of ints
        K-values to try for KNN model.
    weights : string
        Type of weighting to use for KNN model ('distance' or 'uniform')
    train_df : Pandas dataframe
        Data to use for training the KNN model.
        X coordinates are the 'lat' and 'lon' columns.
        Y values (predicted types) are the 'type' column.
    test_df : Pandas dataframe
        Data to use for test the KNN model.
        X coordinates are the 'lat' and 'lon' columns.
        Y values (predicted types) are the 'type' column.

    Returns
    -------
    errors : array
        First column: ints, the input list of K values.
        Second column: floats, training error rate for KNN with each K.
        Third column: floats, testing error rate for KNN with each K.

    """
    errors = np.zeros((len(k_list), 3))
    for i in range(len(k_list)):
        k_errors = try_k(k_list[i], weights, train_df, test_df)
        errors[i, 0] = k_list[i]
        errors[i, 1] = k_errors[0]
        errors[i, 2] = k_errors[1]
    return errors


def plot_knn_error(k_max, weights, train_df, test_df):
    """
    Plot training and testing error rate vs K.

    Parameters
    ----------
    k_max : int
        Maximum K-value (K = 1 to k_max will be used).
    weights : string
        Type of weighting to use for KNN model ('distance' or 'uniform')
    train_df : Pandas dataframe
        Data to use for training the KNN model.
        X coordinates are the 'lat' and 'lon' columns.
        Y values (predicted types) are the 'type' column.
    test_df : Pandas dataframe
        Data to use for test the KNN model.
        X coordinates are the 'lat' and 'lon' columns.
        Y values (predicted types) are the 'type' column.


    """
    result = try_k_range(list(range(1, k_max)), weights, train_df, test_df)
    plt.figure(figsize=(4, 4))
    k = result[:, 0]
    train_error = result[:, 1]
    test_error = result[:, 2]
    plt.scatter(k, train_error, color='red', label='Training error')
    plt.scatter(k, test_error, label='Testing error')
    plt.xlabel('K')
    plt.ylabel('Error rate')
    plt.ylim(0, 1)


def geojson_predict_k(geo_df, gen_train, stor_train, k):
    """
    Predict generation and storage types for all features in a dataframe.

    Parameters
    ----------
    geo_df : Pandas dataframe
        dataframe containing geographic features, with a column 'centers'
        which has (latitude, longitude) tuples
        This should be the output of geojson_to_df after modification by
        geojson_centers.
    gen_train : Pandas dataframe
        Data to use for training the generation KNN model.
        X coordinates are the 'lat' and 'lon' columns.
        Y values (predicted types) are the 'type' column.
    stor_train : Pandas dataframe
        Data to use for training the storage KNN model.
        X coordinates are the 'lat' and 'lon' columns.
        Y values (predicted types) are the 'type' column.
    k : int
        Number of nearest-neighbors to consider in KNN model.

    Returns
    -------
    None

    Side Effects
    ------------
    Adds two columns 'pred_gen' and 'pred_stor' to the input geo dataframe,
    containing the predicted energy generation and storage types for each
    feature, based on predicted types for the latitude and longitude
    in the 'centers' column, based on KNN with the input K.

    """

    gen_clf = KNeighborsClassifier(n_neighbors=k, weights='distance')
    gen_clf.fit(gen_train[['lat', 'lon']], np.ravel(gen_train.type))
    stor_clf = KNeighborsClassifier(n_neighbors=k, weights='distance')
    stor_clf.fit(stor_train[['lat', 'lon']], np.ravel(stor_train.type))
    gens = []
    stors = []
    for index, row in geo_df.iterrows():
        latlon = np.asarray(row.centers).reshape(1, 2)
        gens.append(gen_clf.predict(latlon)[0])
        stors.append(stor_clf.predict(latlon)[0])
    geo_df['pred_gen'] = gens
    geo_df['pred_stor'] = stors
