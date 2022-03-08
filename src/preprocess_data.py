import os
import sys
import pandas as pd
from sklearn import preprocessing
from pathlib import Path


def count_nulls_by_line(df):
    return df.isnull().sum().sort_values(ascending=False)


def null_percent_by_line(df):
    return (df.isnull().sum() / df.isnull().count()).sort_values(ascending=False)


def preprocess_data(DATA_PATH):
    df = pd.read_csv(DATA_PATH)

    zeros_cnt = count_nulls_by_line(df)
    # df.isnull().sum().sort_values(ascending=False)
    percent_zeros = null_percent_by_line(df)
    # (df.isnull().sum() / df.isnull().count()).sort_values(ascending=False)

    missing_data = pd.concat(
        [zeros_cnt, percent_zeros], axis=1, keys=["Total", "Percent"]
    )

    dropList = list(missing_data[missing_data["Percent"] > 0.15].index)

    df.drop(dropList, axis=1, inplace=True)
    df.drop(["Date"], axis=1, inplace=True)
    df.drop(["Location"], axis=1, inplace=True)

    ohe = pd.get_dummies(data=df, columns=["WindGustDir", "WindDir9am", "WindDir3pm"])

    ohe["RainToday"] = df["RainToday"].astype(str)
    ohe["RainTomorrow"] = df["RainTomorrow"].astype(str)

    lb = preprocessing.LabelBinarizer()

    ohe["RainToday"] = lb.fit_transform(ohe["RainToday"])
    ohe["RainTomorrow"] = lb.fit_transform(ohe["RainTomorrow"])
    processed_df = ohe

    cols = processed_df.columns.tolist()
    cols.remove("RainTomorrow")
    cols.append("RainTomorrow")
    processed_df = processed_df[cols]

    cols = processed_df.columns.tolist()

    features_df = processed_df.drop(["RainTomorrow"], axis=1)
    features_df.dropna(inplace=True)
    features_df.to_csv("./data/features.csv", index=False)
    processed_df.dropna(inplace=True)
    processed_df.to_csv(DATA_PATH[:-4] + "_processed.csv", index=False)


if __name__ == "__main__":
    DATA_PATH = Path(__file__).parent.parent / "data" / "weatherAUS.csv"
    preprocess_data(str(DATA_PATH.resolve()))
    print(f"Saved to {str(DATA_PATH.resolve())[:-4]}_processed.csv")
