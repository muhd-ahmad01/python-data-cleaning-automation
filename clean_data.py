import pandas as pd
import sys
import re
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def is_valid_email(email):
    if pd.isna(email):
        return False
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, str(email)))
    

def load_file(file_path):
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)

            # Handle improperly quoted CSV (single column with comma-separated values)
            if len(df.columns) == 1:
                col_name = df.columns[0]
                first_val = df.iloc[0, 0] if not df.empty else ''

                if (isinstance(col_name, str) and ',' in col_name) or \
                   (isinstance(first_val, str) and ',' in first_val):

                    header_vals = col_name.split(',')
                    split_df = df.iloc[:, 0].str.split(',', expand=True)
                    split_df.columns = header_vals
                    return split_df

            return df

        elif file_path.endswith('.xlsx'):
            return pd.read_excel(file_path)

        else:
            raise ValueError("Unsupported file format.")

    except Exception as e:
        logging.error(f"Error loading file: {e}")
        sys.exit(1)


def clean_data(df):
    logging.info("Starting data cleaning process...")

    df = df.drop_duplicates().copy()

    for col in ['Age', 'Salary']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    if 'JoinDate' in df.columns:
        df['JoinDate'] = pd.to_datetime(df['JoinDate'], errors='coerce')
        df['JoinDate'] = df['JoinDate'].dt.strftime('%Y-%m-%d')

    if 'Email' in df.columns:
        df = df[df['Email'].apply(is_valid_email)].copy()

    if 'Age' in df.columns:
        df['Age'] = df['Age'].fillna(df['Age'].median())

    if 'Salary' in df.columns:
        df['Salary'] = df['Salary'].fillna(df['Salary'].median())

    if 'City' in df.columns:
        df['City'] = df['City'].fillna("Unknown")

    logging.info("Data cleaning completed.")
    return df


def save_file(df, input_path):
    base, ext = os.path.splitext(input_path)
    output_path = f"{base}_cleaned{ext}"

    try:
        if ext == '.csv':
            df.to_csv(output_path, index=False)
        else:
            df.to_excel(output_path, index=False)

        logging.info(f"Saved: {output_path}")

    except Exception as e:
        logging.error(f"Error saving file: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("Usage: python clean_data.py <input_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        logging.error("File does not exist.")
        sys.exit(1)

    df = load_file(file_path)
    cleaned_df = clean_data(df)
    save_file(cleaned_df, file_path)


if __name__ == "__main__":
    main()