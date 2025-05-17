import random
import datetime
import uuid
import csv
from decimal import Decimal

def generate_transaction_id(date_str):
    """Generate a transaction ID based on date and a sequential number."""
    # Extract date components from the date string (format: YYYY-MM-DD)
    date_parts = date_str.split('-')
    year = date_parts[0]
    month = date_parts[1]
    day = date_parts[2]

    # Generate a random 2-digit sequence number
    sequence = str(random.randint(1, 99)).zfill(2)

    return f"TXN-{year}{month}{day}{sequence}"

def generate_amount(currency):
    """Generate a random amount with 2 decimal places."""
    # Generate amount between 10 and 10000
    amount = round(random.uniform(10, 10000), 2)
    return f"{currency}{amount:,.2f}"

def generate_timestamp(start_date, end_date):
    """Generate a random timestamp between start_date and end_date."""
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_days = random.randrange(days_between_dates)
    random_seconds = random.randrange(86400)  # Seconds in a day

    random_date = start_date + datetime.timedelta(days=random_days, seconds=random_seconds)
    return random_date.strftime("%Y-%m-%d %H:%M:%S"), random_date.strftime("%Y-%m-%d")

def generate_transaction_type():
    """Generate a random transaction type."""
    transaction_categories = [
        "PAYMENT", "DEPOSIT", "WITHDRAWAL", "TRANSFER", "REFUND", "PURCHASE", "FEE"
    ]

    transaction_methods = [
        "CASH", "CHQ", "CARD", "ONLINE", "TRANSFER-OUT", "TRANSFER-IN", "DIRECT-DEBIT"
    ]

    reference_types = [
        "REF", "ATM", "CHQ", "INV", "POS"
    ]

    category = random.choice(transaction_categories)
    method = random.choice(transaction_methods)
    ref_type = random.choice(reference_types)
    ref_number = str(random.randint(100, 999))

    return f"{category}/{method}/{ref_type}#{ref_number}"

def generate_financial_transactions(num_records, output_file):
    """Generate synthetic financial transaction records."""

    # Define currencies
    currencies = ["$", "€", "£", "¥", "₹"]

    # Define date range (last 30 days)
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=30)

    # Open output file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerow(["Transaction ID", "Amount", "Timestamp", "Description"])

        # Generate records
        for _ in range(num_records):
            # Generate timestamp
            timestamp, date_str = generate_timestamp(start_date, end_date)

            # Generate transaction ID
            txn_id = generate_transaction_id(date_str)

            # Generate amount with random currency
            currency = random.choice(currencies)
            amount = generate_amount(currency)

            # Generate transaction type
            txn_type = generate_transaction_type()

            # Write record
            writer.writerow([txn_id.strip(), amount.strip(), timestamp.strip(), txn_type.strip()])

    print(f"Generated {num_records} financial transaction records in {output_file}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Generate synthetic financial transaction data')
    parser.add_argument('--records', type=int, default=100, help='Number of records to generate')
    parser.add_argument('--output', type=str, default='financial_transactions.csv', help='Output file name')

    args = parser.parse_args()

    generate_financial_transactions(args.records, args.output)