# Runtime Analysis Python

A command-line algorithm runtime analysis tool that performs comparative performance analysis of different sorting algorithms. This educational tool helps demonstrate algorithm complexity and Big O notation in practice.

## Features

- **Interactive CLI Interface**: User-friendly prompts for configuration
- **Algorithm Performance Comparison**: Measures execution time for five different sorting algorithms
- **Random Data Generation**: Creates test datasets of configurable size and range
- **Multiple Test Runs**: Execute multiple iterations for reliable performance metrics
- **Precision Timing**: High-precision timing using `time.perf_counter()`

## Technology Stack

- **Language**: Python 3.10+
- **Dependencies**: None (uses only Python standard library)
- **Core Libraries**: `random`, `time`
- **Architecture**: Modular design with clear separation of concerns

## Algorithms Included

1. **Quick Sort** - O(n log n) average case, recursive divide-and-conquer
2. **Bubble Sort** - O(n²) simple comparison sorting
3. **Insertion Sort** - O(n²) insertion-based sorting  
4. **Merge Sort** - O(n log n) guaranteed, recursive merge sort
5. **Python Sort** - Wrapper for Python's built-in Timsort algorithm

## Installation & Setup

### Prerequisites
- Python 3.x installed on your system
- No additional package installations required

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/whiletrace/runtime-analysis-python.git
   cd runtime-analysis-python
   ```

2. Run the application:
   ```bash
   python3 runtime_analysis_proj.py
   ```

## Usage

The application will prompt you for three inputs:

1. **List length** - Number of elements to sort (integer)
2. **Maximum number value** - Range for random integers (integer)
3. **Number of test runs** - How many times to execute the test (integer)

### Example Usage

```bash
$ python3 runtime_analysis_proj.py
enter a number for the length of the list 1000
what is the largest number represented 10000
how many times would you like this to run 3

----------------------------------------
Run: 1
Quick_sort    ->Elapsed time: 0.00156 seconds
Bubble_sort   ->Elapsed time: 0.12847 seconds
Insertion_sort->Elapsed time: 0.05692 seconds
Mergesort     ->Elapsed time: 0.00203 seconds
Python_sort   ->Elapsed time: 0.00009 seconds
----------------------------------------
```

## Project Structure

```
runtime-analysis-python/
├── runtime_analysis_proj.py    # Main entry point and CLI interface
├── timer.py                    # Timer utility class
├── demos.py                    # Sorting algorithm implementations
├── LICENSE                     # MIT License
└── README.md                   # Project documentation
```

### Key Files

- **`runtime_analysis_proj.py`** - Main application with user input handling and execution orchestration
- **`timer.py`** - Timer class with high-precision timing and error handling
- **`demos.py`** - Collection of five sorting algorithm implementations

## Core Components

### Timer Class (`timer.py`)
- High-precision timing using `time.perf_counter()`
- Custom `TimerError` exception for proper error handling
- Start/stop functionality with misuse prevention

### Algorithm Collection (`demos.py`)
- Five different sorting algorithms with varying time complexities
- Each algorithm handles list copying to ensure fair comparison
- Implementations follow standard algorithm patterns

### Main Application (`runtime_analysis_proj.py`)
- Interactive user input with error handling
- Random test data generation
- Performance analysis coordination
- Results formatting and display

## Educational Use Cases

- **Computer Science Education**: Demonstrate algorithm complexity concepts
- **Performance Benchmarking**: Compare sorting algorithm efficiency
- **Big O Notation**: Show practical differences between O(n²) and O(n log n) algorithms
- **Algorithm Analysis**: Study how input size affects performance

## Development

### Running Tests
Currently no automated tests are included. The application serves as a demonstration tool rather than production software.

### Contributing
This project serves as an educational tool. Feel free to fork and modify for learning purposes.

## License

MIT License - See LICENSE file for details.

## Author

Trace Harris

---

*This tool demonstrates fundamental computer science concepts and is ideal for educational purposes and algorithm performance analysis.*