from typing import final

import openpyxl

from .parser import BaseParser


class XLSXParser(BaseParser):
    @final
    def parse_sheet(self):
        workbook = openpyxl.load_workbook(self.file_path)
        num_worksheets = len(workbook.worksheets)

        for worksheet in workbook.worksheets:
            print(worksheet)
            for row in range(worksheet.max_row):
                if row == 0:
                    self.table_data["header"] = (
                        cell.value for cell in worksheet[row + 1]
                    )
