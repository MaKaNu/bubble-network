from abc import ABC, abstractmethod
from typing import Any, Dict, final
from pathlib import Path


class Renderer(ABC):
    @final
    def __init__(self):
        pass


#    @abstractmethod
#    def parse_sheet(self):
#        ...
