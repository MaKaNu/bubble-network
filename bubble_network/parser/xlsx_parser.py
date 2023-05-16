from typing import final, Tuple

import openpyxl
from openpyxl.cell.cell import Cell

from .parser import BaseParser


class XLSXParser(BaseParser):
    @final
    def parse_sheet(self):
        workbook = openpyxl.load_workbook(self.file_path)

        for worksheet in workbook.worksheets:
            for row in range(worksheet.max_row):
                row_cell_tuple = worksheet[row + 1]
                if row == 0:
                    self.table_data[worksheet.title] = {
                        "header": self.row2tuple(row_cell_tuple)
                    }
                    self.table_data[worksheet.title]["rows"] = []
                else:
                    self.table_data[worksheet.title]["rows"].append(
                        self.row2tuple(row_cell_tuple)
                    )

    @staticmethod
    def row2tuple(row: Tuple[Cell]) -> Tuple[str | int]:
        return tuple(cell.value for cell in row)
