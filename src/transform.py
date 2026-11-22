import logging
import pandas as pd

logger = logging.getLogger(__name__)

def to_df(raw_data: dict[dict]) -> pd.DataFrame:
    """
    Generate dataframe from raw prices data
    """

    records = []
    for symbol, data in raw_data.items():
        for d_price in data["values"]:
            d_price["date"] = d_price.pop("datetime")
            d_price["symbol"] = symbol
            records.append(d_price)

    df = pd.DataFrame(records)
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df.set_index("date")