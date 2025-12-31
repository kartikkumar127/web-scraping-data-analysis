import pandas as pd
import re

# Load raw data with encoding fix
df = pd.read_csv("books_raw.csv", encoding="latin1")

# CLEAN PRICE COLUMN

def clean_price(value):
    if pd.isna(value):
        return None
    value = str(value)
    value = re.sub(r"[^\d.]", "", value)  # remove all non-numeric characters
    return float(value) if value else None

df["Price"] = df["Price"].apply(clean_price)

# CLEAN RATING COLUMN
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
df["Rating"] = df["Rating"].map(rating_map)

# CLEAN AVAILABILITY
df["Availability"] = (
    df["Availability"]
    .astype(str)
    .str.replace("\n", "")
    .str.replace("In stock", "Yes")
    .str.strip()
)

# REMOVE DUPLICATES & NULLS
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# SAVE CLEAN DATA
df.to_csv("books_cleaned.csv", index=False)

print("Data cleaned successfully and saved as book")

