# Lesson 4: Forex Project

Fetching daily forex data from Twelve API to load raw JSON and output CSV

## Install

```bash
pip install -r requirements.txt
```
## Run

```bash
python main.py --symbols XAU/USD,EUR/USD --period 100
```

Parameters

| Parameter | Default | Description |
|---|---|---|
| `symbols` | `XAU/USD` | Trading Instrument Symbol List (separated by comma) |
| `period` | 30 | Number of days to retrieve daily data for |
| `raw` | `full_draws.json` | Raw JSON File |
| `output-csv` | `xsmb_results.csv` | Output CSV File |


## Project Structure

```
ls04/
├── requirements.txt
├── main.py            # CLI entry point
└── src/
    ├── config.py       # Configure
    ├── api_client.py   # Call API
    ├── storage.py       # Read/Write JSON file and CSV file
    └── transform.py     # Generate Dataframe
    └── utils.py     # Retry Decorator
```