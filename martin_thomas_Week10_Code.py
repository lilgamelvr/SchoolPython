#  Original code from https://sunscrapers.com/blog/streamlit-dash-panel-features-part-2/

import pandas as pd
import plotly.express as px
from dash import Dash
from dash import Input
from dash import Output
from dash import callback
from dash import dcc
from dash import html

df: pd.DataFrame = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv")

app: Dash = Dash(__name__)

app.layout = html.Div(
    [
        html.H1(children="Assignment 9: Population by Year", style={"textAlign": "center"}),
        dcc.Dropdown(df.country.unique(), "Canada", id="dropdown-selection"),
        dcc.Graph(id="graph-content"),
    ]
)


@callback(Output("graph-content", "figure"), Input("dropdown-selection", "value"))
def update_graph(value):
    dff: pd.DataFrame = df[df.country == value]
    return px.line(dff, x="year", y="pop")


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1")
