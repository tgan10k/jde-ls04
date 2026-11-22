import logging
import argparse
from dotenv import load_dotenv

from src.config import setup_logging
from src.api_client import fetch_daily_prices
from src.storage import store_json, export_csv
from src.transform import to_df

logger = logging.getLogger(__name__)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Get Daily Forex Data")
    parser.add_argument("--symbols", type=str, default="XAU/USD", help="Instrument Symbol (default: XAU/USD)")
    parser.add_argument("--period", type=int, default=30, help="Fetched Period (days) (default: 30)")
    parser.add_argument("--raw", type=str, default="raw.json", help="Raw JSON file path (default: raw.json)")
    parser.add_argument("--output_csv", type=str, default="result.csv", help="Output csv file path (default: result.csv)")

    return parser.parse_args()

def main() -> None:
    load_dotenv()
    setup_logging()
    args = parse_args()

    logger.info(f"Extract daily data in {args.period} days for: \n\t{args.symbols}")
    raw_data = fetch_daily_prices(args.symbols, args.period)

    logger.info(f"Store raw data to JSON file: {args.raw}")
    store_json(raw_data, "data/" + args.raw)
    
    logger.info("Transform raw data ...")
    df = to_df(raw_data)

    export_csv(df, "data/" + args.output_csv)
    logger.info(f"Successfully stored {len(df)} daily price records to {args.output_csv} file for: \n\t{args.symbols}")
    

if __name__ == "__main__":
    main()