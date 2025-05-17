# Python Assignment: Financial Transaction Log Parser

## Background
In the financial industry, processing and analyzing transaction logs is a crucial task. Banks and financial institutions deal with large volumes of transaction data that need to be parsed, validated, and analyzed efficiently . This assignment will focus on automating the extraction of information from bank transaction logs using Python regex.

## Assignment Overview
You will create a Python program that processes a bank transaction log file containing various transaction records. The program should extract and validate specific patterns of information using regular expressions.

## Learning Objectives
- Implement regex patterns to extract financial data
- Process real-world transaction log formats
- Validate financial data formats
- Handle multiple data patterns simultaneously
- Apply error handling for invalid data formats

## Dataset Description
The input file will be a text file containing transaction records with the following formats:

```
TXN-2025051701 | $1,234.56 | 2025-05-17 01:45:23 | PAYMENT/TRANSFER-OUT/REF#789
TXN-2025051702 | €2,345.67 | 2025-05-17 02:15:00 | DEPOSIT/CASH/ATM#456
TXN-2025051703 | £3,456.78 | 2025-05-17 02:29:30 | WITHDRAWAL/CHQ#123
```

## Required Tasks

### 1. Transaction ID Validation
Create a regex pattern to validate transaction IDs that follow the format:
- Starts with "TXN-" followed by 10 digits
- Example pattern: `TXN-2025051701`


### 2. Currency Amount Extraction
Implement regex patterns to extract and validate currency amounts:
- Support for multiple currency symbols ($, €, £)
- Proper formatting with thousands separator (comma)
- Two decimal places
- Example formats: `$1,234.56`, `€2,345.67`, `£3,456.78`


### 3. Timestamp Validation
Create a regex pattern to validate timestamps in the format:
- YYYY-MM-DD HH:MM:SS
- Ensure valid date and time ranges
- Example: `2025-05-17 02:29:30`

### 4. Transaction Type Classification
Implement regex patterns to categorize transactions based on their descriptions:
- PAYMENT/TRANSFER
- DEPOSIT
- WITHDRAWAL
- Extract reference numbers (REF#, ATM#, CHQ#)

## Advanced Requirements

### 5. Data Analysis
Create functions to:
- Calculate total transaction amounts per currency
- Generate summary statistics for different transaction types
- Identify patterns in transaction timing

### 6. Error Handling
Implement robust error handling for:
- Malformed transaction IDs
- Invalid currency formats
- Incorrect timestamps
- Missing or incomplete data

## Deliverables
1. Python script containing the implementation
2. Test cases demonstrating functionality
3. Documentation explaining regex patterns used
4. Sample output showing processed results

## Evaluation Criteria
- Correct implementation of regex patterns
- Proper handling of edge cases
- Code organization and documentation
- Performance with large datasets
- Error handling implementation