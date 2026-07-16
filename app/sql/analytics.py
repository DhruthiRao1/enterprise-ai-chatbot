import pandas as pd

df = pd.read_csv("app/data/sample_sales.csv")


def get_total_sales(year):
    return float(
        df[df["Year"] == year]["Sales"].sum()
    )


def compare_sales_last_3_years():

    sales = (
        df.groupby("Year")["Sales"]
        .sum()
        .reset_index()
    )

    return sales.to_dict("records")


def get_highest_growth_region():

    region_sales = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
    )

    top_region = region_sales.sort_values(
        "Sales",
        ascending=False
    ).iloc[0]

    return top_region["Region"]


def get_quarterly_sales():

    quarterly = (
        df.groupby("Quarter")["Sales"]
        .sum()
        .reset_index()
    )

    return quarterly.to_dict("records")


def get_top_products():

    products = (
        df.groupby("Product")["Sales"]
        .sum()
        .reset_index()
        .sort_values(
            "Sales",
            ascending=False
        )
    )

    return products.to_dict("records")


def summarize_sales_report():

    total_sales = df["Sales"].sum()

    top_product = (
        df.groupby("Product")["Sales"]
        .sum()
        .idxmax()
    )

    top_region = (
        df.groupby("Region")["Sales"]
        .sum()
        .idxmax()
    )

    return (
        f"Total revenue was {total_sales}. "
        f"Top product was {top_product}. "
        f"Top region was {top_region}."
    )
