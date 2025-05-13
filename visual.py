from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

# Load and prepare data
df = pd.read_csv("processed.csv")
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Sales Data (Pink Morsel)",
    labels={"Sales": "Sales Amount", "Date": "Date"}
)

# Layout
app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Visualizer'),
    dcc.Graph(id='sales-line-chart', figure=fig)
], style={'padding': '20px'})

if __name__ == '__main__':
    app.run(debug=True)
