# Python Assignment: Global Logistics Data Parser and Validator

## Background
Modern logistics companies handle diverse shipping documents, tracking numbers, and product codes across multiple carriers and countries. This assignment simulates a real-world scenario where you'll build a system to process and validate various logistics data formats using regular expressions.

## Assignment Overview
Create a Python program that processes multiple logistics document formats, validates tracking numbers across different carriers, and handles product identification codes while ensuring compliance with international shipping standards.

## Learning Objectives
- Master complex regex patterns for varied data formats
- Implement multi-format validation systems
- Handle international shipping document processing
- Build robust error handling for diverse data scenarios
- Perform advanced data analysis and reporting

## Dataset Description
The input will consist of multiple files containing:

### 1. Tracking Numbers File
```
1Z999AA1234567890 | UPS | 2025-05-17 | DELIVERED
270980930989777 | FEDEX | 2025-05-16 | IN_TRANSIT
42389023| DHL | 2025-05-15 | PROCESSING
```

### 2. Product Codes File
```
UPC-A: 123456789012 | SKU: ABC-123-XL-BLK | EAN: 5901234123457
GTIN: 10614141000415 | SKU: XYZ-456-M-RED | EAN: 4007817000000
```

### 3. Shipping Documents
```
AWB: 172-12345675 | ORIGIN: US | DEST: UK | WEIGHT: 125.5KG
BOL: MAEU123456789 | VESSEL: MAERSK SEALAND | CONTAINERS: MSKU1234567
INV: CI-2025-12345 | VALUE: $5,432.10 | HS CODE: 8471.30.0100
```

## Required Tasks

### 1. Carrier Tracking Number Validation
Implement regex patterns to validate tracking numbers for multiple carriers :
- UPS (1Z + 16 characters)
- FedEx (12, 14, or 22 digits)
- DHL (10 digits)
- Handle variations in format and length

### 2. Product Code Processing
Create regex patterns to extract and validate   :
- UPC-A (12 digits with check digit)
- EAN-13 (13 digits with country code)
- GTIN-14 (14 digits)
- Custom SKU formats (alphanumeric with variable patterns)

### 3. Shipping Document Processing
Implement validation for shipping documents   :
- Air Waybill (AWB) numbers
- Bill of Lading (BOL) numbers
- Commercial Invoice numbers
- Extract relevant shipping details (origin, destination, weight, value)

### 4. Data Compliance Validation
Implement compliance checks  :
- Verify document completeness
- Validate date formats across time zones
- Check for required fields in shipping documents
- Ensure proper format of customs declarations

## Advanced Requirements

### 5. Complex Data Analysis
Create functions to:
- Generate shipping trends by carrier
- Calculate value distribution by destination
- Analyze product code distribution
- Track compliance violations

### 6. Error Handling and Logging
Implement sophisticated error handling for:
- Invalid tracking number formats
- Mismatched product codes
- Incomplete shipping documents
- Compliance violations
- Create detailed error logs with timestamps

### 7. Data Transformation
Create functions to:
- Convert between different product code formats
- Standardize shipping document formats
- Generate normalized data structures
- Create compliance reports

## Deliverables
1. Python modules for each component
2. Comprehensive test suite
3. Documentation including:
   - Regex pattern explanations
   - Validation rules
   - Compliance requirements
4. Sample data processor
5. Analysis reports generator

## Evaluation Criteria
- Accuracy of regex pattern matching
- Handling of international formats
- Compliance with shipping standards
- Code organization and modularity
- Performance with large datasets
- Quality of error handling
- Documentation completeness

## Bonus Challenges
1. Implement real-time validation API
2. Create GUI for document processing
3. Add support for additional carriers
4. Implement machine learning for pattern recognition
5. Create visualization of shipping networks
