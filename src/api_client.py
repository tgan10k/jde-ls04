import os
import logging
import requests

from src.utils import retry

logger = logging.getLogger(__name__)

@retry(retries = 3, delay = 2, logger = logger)
def fetch_daily_prices(symbols: str = "XAU/USD", period: int = 30) -> dict[dict]:
    """Fetch latest daily prices of trading instrument from API 
    Args:
        symbols (str): list of instrument symbols
        period (int): days
        
    Returns:
        dict[dict]: daily prices of trading instruments
    """

    url = os.getenv("DATA12_API_URL")
    headers = {
        "x-rapidapi-key": os.getenv("DATA12_API_KEY"),
        "x-rapidapi-host": os.getenv("DATA12_API_HOST")
    }
    q_params = {
        "outputsize":period,
        "format":"json",
        "symbol":symbols,
        "interval":"1day"
    }
    response = requests.get(url, headers=headers, params=q_params)

    if not "," in symbols:
        return {symbols: response.json()}
    return response.json()
