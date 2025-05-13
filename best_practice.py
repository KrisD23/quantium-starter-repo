# This files contains the best practices for a dash application

import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Constants
DATA_PATH = "./processed.csv"
COLORS = {
    "primary": "#FEDBFF",
    "secondary": "#D598EB",
    "font": "#522A61"
}

# Load and prepare data
data = pd.read_csv(DATA_PATH)
data['Date'] = pd.to_datetime(data['Date'])  # Ensure datetime type
data = data.sort_values(by="Date")

# Initialize Dash app
dash_app = Dash(__name__)

# Generate figure function
def generate_figure(chart_data):
    fig = px.line(chart_data, x="Date", y="Sales", title="Pink Morsel Sales")
    fig.update_layout(
        plot_bgcolor=COLORS["secondary"],
        paper_bgcolor=COLORS["primary"],
        font_color=COLORS["font"]
    )
    return fig

# Initial figure
visualization = dcc.Graph(
    id="visualization",
    figure=generate_figure(data)
)

# Header
header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={
        "background-color": COLORS["secondary"],
        "color": COLORS["font"],
        "border-radius": "20px",
        "padding": "10px"
    }
)

# Region radio buttons
region_picker = dcc.RadioItems(
    options=[
        {"label": "North", "value": "north"},
        {"label": "East", "value": "east"},
        {"label": "South", "value": "south"},
        {"label": "West", "value": "west"},
        {"label": "All", "value": "all"},
    ],
    value="all",
    id="region_picker",
    inline=True,
    style={"marginBottom": "20px"}
)
region_picker_wrapper = html.Div([region_picker], style={"font-size": "150%"})

# Callback to update graph
@dash_app.callback(
    Output("visualization", "figure"),
    Input("region_picker", "value")
)
def update_graph(region):
    if region == "all":
        trimmed_data = data
    else:
        trimmed_data = data[data["Region"] == region]
    return generate_figure(trimmed_data)

# Layout
dash_app.layout = html.Div(
    [header, region_picker_wrapper, visualization],
    style={
        "textAlign": "center",
        "background-color": COLORS["primary"],
        "border-radius": "20px",
        "padding": "30px",
        "fontFamily": "Arial, sans-serif"
    }
)

# Run the server
if __name__ == '__main__':
    dash_app.run(debug=True)
