# Data Structures Practice Assignments for Data Engineering Interviews

## Assignment 1: String Processing - Log Parser
```python
class LogParser:
    def __init__(self):
        self.logs = []
    
    def parse_log_line(self, line: str) -> dict:
        """
        Parse a log line in the format:
        2025-05-17 03:08:45 | ERROR | user_id=123 | message="Failed to process data"
        Return a dictionary with timestamp, level, user_id, and message
        """
        pass
    
    def filter_logs_by_level(self, level: str) -> list:
        """Return all logs of a specific level (ERROR, INFO, WARNING)"""
        pass
    
    def get_user_error_count(self) -> dict:
        """Return dictionary with user_id as key and their error count as value"""
        pass
```

**Learning Focus:**
- String manipulation
- Regular expressions
- Dictionary operations
- Time complexity: O(n) for parsing

## Assignment 2: List Operations - Data Deduplication
```python
class DataDeduplicator:
    def __init__(self):
        self.data = []
    
    def add_records(self, records: list) -> None:
        """Add new records while maintaining uniqueness"""
        pass
    
    def remove_duplicates(self) -> list:
        """Remove duplicates while preserving order"""
        pass
    
    def find_most_frequent(self, k: int) -> list:
        """Return k most frequent elements"""
        pass
    
    def get_running_median(self) -> float:
        """Calculate running median of the dataset"""
        pass
```

**Learning Focus:**
- List operations
- Set operations
- Sorting algorithms
- Time complexity analysis

## Assignment 3: Stack Implementation - ETL Validator
```python
class ETLValidator:
    def __init__(self):
        self.operation_stack = []
        self.undo_stack = []
    
    def push_operation(self, operation: str) -> None:
        """Add new ETL operation to stack"""
        pass
    
    def validate_dependencies(self) -> bool:
        """Check if operations are in valid order"""
        pass
    
    def undo_last_operation(self) -> str:
        """Remove and return last operation"""
        pass
    
    def get_operation_history(self) -> list:
        """Return list of all operations in order"""
        pass
```

**Learning Focus:**
- Stack operations
- LIFO principle
- Error handling
- Time complexity: O(1) for push/pop

## Assignment 4: Linked List - Data Pipeline
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DataPipeline:
    def __init__(self):
        self.head = None
    
    def add_transformation(self, transform_func) -> None:
        """Add new transformation to pipeline"""
        pass
    
    def remove_transformation(self, transform_name: str) -> bool:
        """Remove transformation from pipeline"""
        pass
    
    def execute_pipeline(self, data: list) -> list:
        """Execute all transformations in order"""
        pass
    
    def reverse_pipeline(self) -> None:
        """Reverse the order of transformations"""
        pass
```

**Learning Focus:**
- Linked list operations
- Pointer manipulation
- Memory management
- Time complexity analysis

## Assignment 5: Dictionary - Data Catalog
```python
class DataCatalog:
    def __init__(self):
        self.catalog = {}
        self.metadata = {}
    
    def add_dataset(self, dataset_id: str, metadata: dict) -> None:
        """Add new dataset with metadata"""
        pass
    
    def update_metadata(self, dataset_id: str, updates: dict) -> bool:
        """Update metadata for existing dataset"""
        pass
    
    def search_datasets(self, criteria: dict) -> list:
        """Search datasets matching given criteria"""
        pass
    
    def get_dataset_lineage(self, dataset_id: str) -> dict:
        """Return dataset dependencies and lineage"""
        pass
```

**Learning Focus:**
- Dictionary operations
- Hash table concepts
- Search optimization
- Time complexity: O(1) average case

## Testing Template
```python
import unittest

class DataStructureTests(unittest.TestCase):
    def setUp(self):
        # Initialize test data
        pass
    
    def test_normal_case(self):
        # Test normal operation
        pass
    
    def test_edge_cases(self):
        # Test edge cases
        pass
    
    def test_error_conditions(self):
        # Test error conditions
        pass
    
    def test_performance(self):
        # Test performance with large datasets
        pass
```

## Implementation Guidelines:
1. Focus on time and space complexity
2. Handle edge cases properly
3. Include proper error handling
4. Add documentation and comments
5. Write comprehensive tests

## Evaluation Criteria:
1. Correctness of implementation
2. Code efficiency
3. Error handling
4. Test coverage
5. Code organization