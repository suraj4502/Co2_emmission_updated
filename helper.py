import streamlit as st
import pandas as pd


st.cache
def get_Data(filename):
    df = pd.read_csv(filename,sep=';')
    return df
st.cache
def get_Data1(filename):
    df = pd.read_csv(filename)
    return df

def preprocessing1(df, variable):
    df = df.drop_duplicates()
    percentile25 = df[variable].quantile(0.25)
     # print(percentile25)
    percentile75 = df[variable].quantile(0.75)
    # print(percentile75)
    iqr = percentile75 - percentile25
    # print(iqr)
    upper_limit = percentile75 + 1.5 * iqr
    # print(upper_limit)
    lower_limit = percentile25 - 1.5 * iqr
    # print(lower_limit)
    # removing
    new_df = df[(df[variable]) < (upper_limit)]
    #print(new_df.shape)
    return new_df