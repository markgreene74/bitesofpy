# https://codechalleng.es/bites/140/
import pandas as pd

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


def athletes_most_medals(data=data):
    # load the dataset
    df = pd.read_csv(data)

    # create two separate df, groupby athlete
    # m
    men = df["Gender"] == "Men"
    df_men = df[men].groupby("Athlete").count()
    # w
    women = df["Gender"] == "Women"
    df_women = df[women].groupby("Athlete").count()

    # for each df get the name of the athlete with most medals
    # (which is the index) and the number of medals
    m_index, m_value = df_men.idxmax().Medal, df_men.max().Medal
    w_index, w_value = df_women.idxmax().Medal, df_women.max().Medal

    # return as a dict
    return {m_index: m_value, w_index: w_value}
