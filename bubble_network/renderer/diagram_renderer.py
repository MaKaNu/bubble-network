from abc import abstractmethod
from typing import final
import plotly.graph_objects as go

from renderer import Renderer

from parser.parser import BaseParser


class BubbleDiagramRenderer(Renderer):
    @final
    def draw_network_bubble(self, parser: BaseParser):
        data = parser.table_data
        fig = go.Figure()
        network_size = self.calculate_network(data)
        fig.add_trace(
            go.Scatter(
                x=[1.5],
                y=[0.75],
                text=[list(data.keys())[0]],
                mode="text",
            )
        )
        fig.update_layout(width=800, height=800)

        fig.show()

    @staticmethod
    def calculate_network(data):
        pass
