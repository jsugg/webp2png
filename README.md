# webp2png

A module to convert all `.webp` files in a directory to `.png` files using multithreading for improved performance.

## Project Structure

```
webp2png/
│
├── webp2png/
│   ├── __init__.py
│   ├── converter.py
│   ├── utils.py
│   └── config.py
│
├── tests/
│   ├── __init__.py
│   └── test_converter.py
│
├── scripts/
│   └── main.py
│
├── README.md
└── requirements.txt
```

## Installation

1. Clone the repository.
2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the main script to convert `.webp` files to `.png` files.

```sh
python scripts/main.py <directory> [options]
```

### Options

- `--output`: Path to the directory to save `.png` files (default: same as input directory)
- `--threads`: Number of threads to use for conversion (default: auto-detect)
- `--retries`: Number of retries for conversion in case of failure (default: 3)
- `--compression`: Compression level for PNG output (0-9, default: 6)
- `--log-level`: Logging level (default: INFO)
- `--retry-delay`: Delay between retries in seconds (default: 1)
- `--dry-run`: Simulate the conversion process without performing any conversions

## Testing

Run the unit tests using `unittest`:

```sh
python -m unittest discover tests
```

## License

This project is licensed under the MIT License.
