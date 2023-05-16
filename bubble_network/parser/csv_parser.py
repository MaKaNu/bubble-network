import csv
from typing import final, Tuple

import openpyxl
from openpyxl.cell.cell import Cell

from .parser import BaseParser


class CSVParser(BaseParser):
    @final
    def parse_sheet(self):
        sheet_name = self.file_path.stem
        with open(self.file_path, "r", encoding="utf-8") as csv_file:
            csv_reader = tuple(csv.reader(csv_file, delimiter=";"))
            for row, line in enumerate(csv_reader):
                if row == 0:
                    self.table_data[sheet_name] = {"header": tuple(line)}
                    self.table_data[sheet_name]["rows"] = []
                else:
                    self.table_data[sheet_name]["rows"].append(
                        tuple(self.lazy_str2int(val) for val in line)
                    )

    @staticmethod
    def lazy_str2int(value: str) -> str | int:
        if value.isdigit():
            return int(value)
        return value
