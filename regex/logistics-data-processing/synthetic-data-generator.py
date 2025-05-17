import random
from faker import Faker
from datetime import datetime, timedelta
import csv
import string
from typing import List, Dict
import pandas as pd
import numpy as np

# Initialize Faker
fake = Faker()

class LogisticsDataGenerator:
    def __init__(self):
        self.carriers = ['UPS', 'FEDEX', 'DHL']
        self.status = ['DELIVERED', 'IN_TRANSIT', 'PROCESSING', 'DELAYED', 'EXCEPTION']
        self.origins = ['US', 'UK', 'CN', 'DE', 'FR', 'JP', 'AU']
        self.vessels = ['MAERSK SEALAND', 'MSC OSCAR', 'CMA CGM', 'EVERGREEN']
        
    def generate_ups_tracking(self) -> str:
        """Generate UPS style tracking number"""
        return f"1Z{''.join(random.choices(string.ascii_uppercase + string.digits, k=16))}"
    
    def generate_fedex_tracking(self) -> str:
        """Generate FedEx style tracking number"""
        length = random.choice([12, 14, 22])
        return ''.join(random.choices(string.digits, k=length))
    
    def generate_dhl_tracking(self) -> str:
        """Generate DHL style tracking number"""
        return ''.join(random.choices(string.digits, k=10))
    
    def generate_tracking_number(self, carrier: str) -> str:
        """Generate carrier-specific tracking number"""
        if carrier == 'UPS':
            return self.generate_ups_tracking()
        elif carrier == 'FEDEX':
            return self.generate_fedex_tracking()
        else:
            return self.generate_dhl_tracking()
    
    def generate_product_code(self) -> Dict:
        """Generate product identification codes"""
        upc = ''.join(random.choices(string.digits, k=12))
        sku = f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}-{random.randint(100,999)}-{random.choice(['S','M','L','XL'])}-{random.choice(['BLK','RED','BLU','GRN'])}"
        ean = ''.join(random.choices(string.digits, k=13))
        gtin = ''.join(random.choices(string.digits, k=14))
        
        return {
            'UPC-A': upc,
            'SKU': sku,
            'EAN': ean,
            'GTIN': gtin
        }
    
    def generate_shipping_document(self) -> Dict:
        """Generate shipping document details"""
        awb = f"{random.randint(100,999)}-{random.randint(10000000,99999999)}"
        bol = f"MAEU{''.join(random.choices(string.digits, k=9))}"
        container = f"MSKU{''.join(random.choices(string.digits, k=7))}"
        weight = round(random.uniform(0.5, 2000.0), 2)
        value = round(random.uniform(100, 10000), 2)
        
        return {
            'AWB': awb,
            'BOL': bol,
            'CONTAINER': container,
            'WEIGHT': weight,
            'VALUE': value,
            'ORIGIN': random.choice(self.origins),
            'DESTINATION': random.choice(self.origins),
            'VESSEL': random.choice(self.vessels)
        }

    def generate_tracking_data(self, num_records: int) -> List[Dict]:
        """Generate tracking records with controlled anomalies"""
        records = []
        base_date = datetime.now()
        
        for _ in range(num_records):
            carrier = random.choice(self.carriers)
            # Introduce some anomalies (5% chance)
            if random.random() < 0.05:
                tracking = 'INVALID-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            else:
                tracking = self.generate_tracking_number(carrier)
            
            date = base_date - timedelta(days=random.randint(0, 30))
            
            records.append({
                'tracking_number': tracking,
                'carrier': carrier,
                'date': date.strftime('%Y-%m-%d'),
                'status': random.choice(self.status)
            })
        
        return records

def main():
    # Initialize generator
    generator = LogisticsDataGenerator()
    
    # Generate tracking data
    print("Generating tracking data...")
    tracking_records = generator.generate_tracking_data(1000)
    df_tracking = pd.DataFrame(tracking_records)
    df_tracking.to_csv('tracking_numbers.csv', index=False)
    
    # Generate product codes
    print("Generating product codes...")
    product_records = [generator.generate_product_code() for _ in range(500)]
    df_products = pd.DataFrame(product_records)
    df_products.to_csv('product_codes.csv', index=False)
    
    # Generate shipping documents
    print("Generating shipping documents...")
    shipping_records = [generator.generate_shipping_document() for _ in range(750)]
    df_shipping = pd.DataFrame(shipping_records)
    df_shipping.to_csv('shipping_documents.csv', index=False)
    
    # Generate some invalid data for testing error handling
    print("Generating invalid data samples...")
    invalid_records = []
    for _ in range(50):
        invalid_record = {
            'tracking_number': 'INVALID-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)),
            'carrier': random.choice(['INVALID', 'UPS', 'FEDEX', 'DHL']),
            'date': 'INVALID-DATE',
            'status': 'UNKNOWN'
        }
        invalid_records.append(invalid_record)
    
    df_invalid = pd.DataFrame(invalid_records)
    df_invalid.to_csv('invalid_records.csv', index=False)
    
    print("Data generation complete!")
    print(f"Generated files:")
    print(f"- tracking_numbers.csv: {len(tracking_records)} records")
    print(f"- product_codes.csv: {len(product_records)} records")
    print(f"- shipping_documents.csv: {len(shipping_records)} records")
    print(f"- invalid_records.csv: {len(invalid_records)} records")

if __name__ == "__main__":
    main()