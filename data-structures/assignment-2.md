# Python Data Structure Assignments for Data Engineering Interview Preparation

These assignments cover fundamental data structures often encountered in data engineering tasks and interviews. 
Focus on understanding the properties of each structure and choosing the most efficient approach for each problem.
---

## 1. Strings: Data Parsing and Cleaning
**Assignment:** Extract Structured Data from Log Lines
**Problem:** You are given a list of log file lines, each containing semi-structured data. Each line follows a pattern like 
Timestamp - Level - Message: key=value, key2=value2, .... Your task is to parse these lines and extract the timestamp, level, message, and all key-value pairs into a structured format (e.g., a list of dictionaries).

**Input:** A list of strings, where each string is a log line.

**Output:** A list of dictionaries, where each dictionary represents a parsed log entry.
Example:
```
Input: [
    "2023-10-27 10:00:01 - INFO - User login: user_id=123, status=success",
    "2023-10-27 10:01:05 - ERROR - Database connection failed: db=primary, error_code=500"
]
Output: [
    {'timestamp': '2023-10-27 10:00:01', 'level': 'INFO', 'message': 'User login', 'details': {'user_id': '123', 'status': 'success'}},
    {'timestamp': '2023-10-27 10:01:05', 'level': 'ERROR', 'message': 'Database connection failed', 'details': {'db': 'primary', 'error_code': '500'}}
]
```
**Considerations:** Handle lines that might not perfectly match the pattern, missing key-value pairs, or variations in spacing. You might need to use string splitting, stripping, and potentially regular expressions (though try solving it with basic string methods first).

## 2. Lists: Data Aggregation and Transformation
**Assignment:** Process Batched Sensor Data

**Problem:** You receive sensor readings in batches, represented as a list of numerical values. Write a Python function that takes a list of these batches (a list of lists) and performs two tasks:

**Task1:**
Calculate the average reading for each individual batch.

**Task2:**
Find the overall maximum reading across all batches.
```
Input: A list of lists of numbers (e.g., [[10, 12, 11], [15, 14, 16, 17], [8, 9]]).

Output: A tuple containing a list of batch averages and the overall maximum value (e.g., ([11.0, 15.5, 8.5], 17)).

Example:
Input: [[10, 12, 11], [15, 14, 16, 17], [8, 9]]
Output: ([11.0, 15.5, 8.5], 17)
```
Considerations: Handle empty batches or an empty list of batches.

## 3. Stack: Dependency Resolution
**Assignment:** Validate Task Dependencies
**Problem:** You are given a list of tasks where some tasks depend on others. The dependencies are represented as pairs [task, depends_on]. Write a Python function that uses a stack to determine if a given sequence of task executions is valid, meaning that all dependencies are met before a task is executed.
```
Input: A list of dependency pairs (e.g., [['B', 'A'], ['C', 'A'], ['D', 'B'], ['D', 'C']]) and a list representing the execution order (e.g., ['A', 'B', 'C', 'D']).

Output: True if the execution order is valid, False otherwise.

Example:
Dependencies: [['B', 'A'], ['C', 'A'], ['D', 'B'], ['D', 'C']]
Execution Order 1: ['A', 'B', 'C', 'D']  Output: True (A is done, then B and C can be done, then D can be done)
Execution Order 2: ['B', 'A', 'C', 'D']  Output: False (B depends on A, but B is before A)
```
Considerations: How to track completed tasks? What data structure can you use alongside the stack?

## 4. Linked List: Processing Data Streams
**Assignment:** Filter and Transform a Data Stream
**Problem:** You are receiving a continuous stream of data, which you can model as a singly linked list where each node contains a data record (e.g., a dictionary). 

Write a Python function that takes the head of such a linked list, filters the records based on a condition (e.g., a specific value in the dictionary), and creates a new linked list containing only the filtered and potentially transformed records.

```
Input: The head node of a singly linked list, a filtering function, and an optional transformation function.

Output: The head node of the new linked list containing the filtered/transformed data.
Implementation Detail: You'll need to define a Node class and work with node references directly.

Example:
# Assume Node class with data and next attributes
# Input Linked List: Node({'value': 10}) -> Node({'value': 25}) -> Node({'value': 15}) -> None
# Filter: value > 12
# Transformation: None (just keep the original data)
# Output Linked List: Node({'value': 25}) -> Node({'value': 15}) -> None
```

Considerations: How to build the new linked list efficiently? Handle an empty input list or a list where no elements match the filter.

## 5. Dictionary: Data Aggregation and Lookup

**Assignment:** Aggregate Sales Data by Product
**Problem:** You have a list of sales transactions, where each transaction is a dictionary with keys like 'product_id', 'quantity', and 'price'. 

Write a Python function that uses a dictionary to aggregate the total quantity sold and total revenue for each product_id.

```
Input: A list of dictionaries representing sales transactions.

Output: A dictionary where keys are product_ids and values are dictionaries containing the total quantity and total revenue for that product.

Example:
Input: [
    {'product_id': 'A', 'quantity': 10, 'price': 5.0},
    {'product_id': 'B', 'quantity': 5, 'price': 10.0},
    {'product_id': 'A', 'quantity': 3, 'price': 5.0},
    {'product_id': 'C', 'quantity': 7, 'price': 2.0},
]
Output: {
    'A': {'total_quantity': 13, 'total_revenue': 65.0},
    'B': {'total_quantity': 5, 'total_revenue': 50.0},
    'C': {'total_quantity': 7, 'total_revenue': 14.0},
}
```

Considerations: What if the input list is empty? Ensure you handle the calculation of total revenue correctly (quantity * price).
