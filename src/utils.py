import time
import logging
import requests
import functools


def retry(retries: int = 3, delay: int = 2, logger = None):
    """Retry Decorator 
    Args:
        retries (int): number of retries
        delay (int): waiting time for next retry (s)
    """
    logger = logger or logging.getLogger(__name__)
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(retries + 1):
                try:
                    return func(*args, **kwargs)
                except (
                    requests.exceptions.Timeout,
                    requests.exceptions.ConnectionError
                ) as conn_err:
                    if attempt == retries:
                        logger.error(f"{type(conn_err).__name__}:")
                        logger.error(conn_err)
                        break
                    time.sleep(delay)
                except requests.exceptions.HTTPError as http_err:
                    if http_err.response.status_code == 429:
                        if attempt == retries:
                            logger.error("HTTP Error:")
                            logger.error(http_err)
                            break
                        time.sleep(delay)
                    else:
                        logger.error(f"HTTP Error - Code {http_err.response.status_code}:")
                        logger.error(http_err)
                except Exception as err:
                    logger.error(f"{type(err).__name__}:")
                    logger.error(err)
                    break
        return wrapper
    return decorator