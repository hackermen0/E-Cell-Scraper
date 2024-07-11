import pandas as pd
from pyhunter import PyHunter
from requests.exceptions import HTTPError

# Replace with your Hunter.io API key
HUNTER_API_KEY = 'your_hunter_api_key'

def get_email_from_hunter(name, company):
    hunter = PyHunter(HUNTER_API_KEY)
    try:
        result = hunter.email_finder(company=company, full_name=name)
        if result['data']:
            return result['data']['email']
        else:
            return None
    except HTTPError as e:
        print(f"HTTP Error: {e}")
        return None

def read_csv(file_path):
    return pd.read_csv(file_path)

def main(input_csv, output_csv):
    df = read_csv(input_csv)
    df['Email'] = df.apply(lambda row: get_email_from_hunter(row['Name'], row['Company']), axis=1)
    df.to_csv(output_csv, index=False)
    print("Email extraction completed. Results saved to:", output_csv)

# Example usage
input_csv = 'input_emails.csv'  # Path to your input CSV file
output_csv = 'output_with_emails.csv'  # Path to save the output CSV file
main(input_csv, output_csv)