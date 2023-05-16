import csv
from typing import final, Tuple

import openpyxl
from openpyxl.cell.cell import Cell

from .parser import BaseParser


class CSVParser(BaseParser):
    @final
    def parse_sheet(self):
        with open(self.file_path, "r", encoding="utf-8") as csv_file:
            csv_reader = tuple(csv.reader(csv_file, delimiter=";"))
            for row, line in enumerate(csv_reader):
                if row == 0:
                    self.table_data["test"] = {
                        "header": self.row2tuple("row_cell_tuple")
                    }
                    self.table_data["test"]["rows"] = []
                else:
                    self.table_data["test"]["rows"].append(self.row2tuple("row_cell_tuple"))
        print()

    @staticmethod
    def row2tuple(row:Tuple[Cell]) -> Tuple[str | int]:
        return tuple(
            cell.value for cell in row
        )
