from pathlib import Path

from parser.xlsx_parser import XLSXParser


if __name__ == "__main__":
    test = Path("./examples/example.xlsx")
    parser = XLSXParser(test)

    parser.parse_sheet()
