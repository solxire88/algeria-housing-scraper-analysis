import pandas as pd
import numpy as np
import csv
import re
import ast

# options
pd.options.display.max_columns = False
chunk = pd.read_csv(
    "../data/raw.csv",
    engine="c",
    sep=",",
    encoding="utf-8",
    on_bad_lines="skip",
    chunksize=11000,
)


def to_integer(s: str) -> pd.Int64Dtype():
    match = re.search(r"(\d+)", s or "")
    return int(match.group(1)) if match else pd.NA


df = chunk.get_chunk(11000)

selected_cols = [
    "title",
    "createdAt",
    "cities",
    "price",
    "smallDescription",
    "store.name",
]

df = df[selected_cols]
df["createdAt"] = pd.to_datetime(df["createdAt"])
df.price = pd.to_numeric(df.price, downcast="integer")

city = (
    pd.json_normalize(df.cities.apply(ast.literal_eval).explode())
    .drop(
        columns=[
            "id",
            "slug",
            "__typename",
            "region.id",
            "region.slug",
            "region.__typename",
        ]
    )
    .rename(columns={"name": "Town", "region.name": "Wilaya"})
)
area = (
    pd.json_normalize(df.smallDescription.apply(ast.literal_eval).explode())
    .drop(columns=["__typename"])
    .rename(columns={"valueText": "Area"})
)

area.Area = area.Area.astype(str)
area.Area = area.Area.apply(to_integer)

df = pd.concat([df, city, area], axis=1)
df = df.drop(columns=["cities", "smallDescription"])

df = df.rename(
    columns={
        "title": "Title",
        "createdAt": "Date",
        "store.name": "Store",
        "price": "Price",
    }
)

df = df.iloc[:11000]
df["FlatType"] = df["Title"].str.extract(r"\b(F\d+)\b", expand=False)

mask = df["Title"].str.contains(
    r"\b(Location|Vente)\b", regex=True, na=False, case=False
)
df = df[~(mask == False)]

mask = df["Title"].str.contains(r"\b(Location)\b", regex=True, na=False, case=False)

df_location = df[mask]
df_vente = df[~mask]

df_location.to_csv("../data/processed_renting.csv", index=False)
df_vente.to_csv("../data/processed_selling.csv", index=False)
