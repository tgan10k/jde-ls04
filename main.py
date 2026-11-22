import logging
import argparse
from dotenv import load_dotenv

from src.config import setup_logging
from src.api_client import fetch_daily_prices

logger = logging.getLogger(__name__)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Get Daily Forex Data")
    parser.add_argument("--symbols", type=str, default="XAU/USD", help="Instrument Symbol (default: XAU/USD)")
    parser.add_argument("--period", type=int, default=30, help="Fetched Period (days) (default: 30)")

    return parser.parse_args()

if __name__ == "__main__":
    load_dotenv()
    setup_logging()
    args = parse_args()

    logger.info(f"Extract daily data in {args.period} days for: \n{args.symbols}")
    raw_data = fetch_daily_prices(args.symbols, args.period)
    