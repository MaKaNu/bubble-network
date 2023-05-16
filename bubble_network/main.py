from pathlib import Path

from parser.xlsx_parser import XLSXParser
from parser.csv_parser import CSVParser


if __name__ == "__main__":
    test = Path("./examples/example.xlsx")
    test2 = Path("./examples/example.CSV")
    parser = XLSXParser(test)
    parser2 = CSVParser(test2)

    parser.parse_sheet()
    parser2.parse_sheet()
