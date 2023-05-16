from abc import ABC, abstractmethod
from typing import Any, Dict, final
from pathlib import Path


class BaseParser(ABC):
    @final
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.table_data: Dict[str, Any] = {}

    @abstractmethod
    def parse_sheet(self):
        ...
