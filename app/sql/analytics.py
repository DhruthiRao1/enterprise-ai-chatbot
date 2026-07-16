import pandas as pd

df = pd.read_csv("app/data/sample_sales.csv")


def get_total_sales(year):

    result = (
        df[df["year"] == year]
        ["revenue"]
        .sum()
    )

    return float(result)


def get_top_region():

    region_sales = (
        df.groupby("region")["revenue"]
        .sum()
        .reset_index()
    )

    top_region = region_sales.sort_values(
        "revenue",
        ascending=False
    ).iloc[0]

    return {
        "region": top_region["region"],
        "revenue": float(top_region["revenue"])
    }
