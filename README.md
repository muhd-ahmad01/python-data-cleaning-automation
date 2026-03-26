# Python Data Cleaning Automation

This project provides a Python-based automated data cleaning pipeline for handling messy datasets efficiently.

## Features

- Removes duplicate records
- Handles missing values using statistical methods
- Validates email formats using regex
- Standardizes inconsistent date formats
- Converts mixed data types into proper numeric formats
- Supports both CSV and Excel files
- Handles improperly formatted CSV files (quoted rows issue)

## Tech Stack

- Python
- Pandas
- Regex

## How to Use

1. Clone the repository:

```bash
git clone https://github.com/your-username/python-data-cleaning-automation.git
cd python-data-cleaning-automation
```

2. Install the required packages

pip install -r requirements.txt

- Make sure your requirements.txt contains:
  pandas
  openpyxl

## Usage

- Run the script from the command line, passing the path to your input file:
  python clean_data.py your_data.csv
- or for excel file:
  python clean_data.py your_data.xlsx

- The cleaned file will be saved in the same directory with \_cleaned appended to the original filename.

## Project Structure

.
├── clean_data.py # Main cleaning script
├── requirements.txt # Python dependencies
├── README.md # This file
└── my_data_cleaned.csv # Example output (not included in repo)
