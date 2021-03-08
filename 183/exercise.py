# https://codechalleng.es/bites/183/
import os
from urllib.request import urlretrieve

import pandas as pd

TMP = os.getenv("TMP", "/tmp")
EXCEL = os.path.join(TMP, "order_data.xlsx")
if not os.path.isfile(EXCEL):
    urlretrieve("https://bites-data.s3.us-east-2.amazonaws.com/order_data.xlsx", EXCEL)


def load_excel_into_dataframe(excel=EXCEL):
    """Load the SalesOrders sheet of the excel book (EXCEL variable)
    into a Pandas DataFrame and return it to the caller"""
    return pd.read_excel(EXCEL, sheet_name="SalesOrders")


def get_year_region_breakdown(df):
    """Group the DataFrame by year and region, summing the Total
    column. You probably need to make an extra column for
    year, return the new df as shown in the Bite description"""
    df = df.rename(columns={"OrderDate": "Year"})
    return df.groupby([(df["Year"].dt.year), "Region"])["Total"].agg("sum")


def get_best_sales_rep(df):
    """Return a tuple of the name of the sales rep and
    the total of his/her sales"""
    _reps = df.groupby("Rep")["Total"].agg("sum")
    return tuple(_reps.reset_index().sort_values(["Total"]).tail(1).values[0])


def get_most_sold_item(df):
    """Return a tuple of the name of the most sold item
    and the number of units sold"""
    _items = df.groupby("Item")["Units"].agg("sum")
    return tuple(_items.reset_index().sort_values(["Units"]).tail(1).values[0])
