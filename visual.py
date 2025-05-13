from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash()

# Load and prepare data
df = pd.read_csv("processed.csv")
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')


regions = ['all'] + sorted(df['Region'].unique())

# App layout
app.layout = html.Div(children=[
    html.H1('Pink Morsel Sales Visualizer', style={
        'textAlign': 'center',
        'color': '#2c3e50',
        'marginBottom': '20px'
    }),

    html.Div([
        html.Label("Select Region:", style={'fontWeight': 'bold'}),
        dcc.RadioItems(
            id='region-radio',
            options=[{'label': r.capitalize(), 'value': r} for r in regions],
            value='all',
            inline=True,
            style={'marginBottom': '20px'}
        )
    ], style={'textAlign': 'center'}),

    dcc.Graph(id='sales-line-chart'),

], style={
    'padding': '40px',
    'fontFamily': 'Arial, sans-serif',
    'backgroundColor': '#f9f9f9',
    'maxWidth': '1000px',
    'margin': '0 auto'
})


# Callback to update chart based on region
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-radio', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['Region'] == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        title=f"Sales Data ({selected_region.capitalize() if selected_region != 'all' else 'All Regions'})",
        labels={"Sales": "Sales Amount", "Date": "Date"},
        template="plotly_white"
    )
    return fig


if __name__ == '__main__':
    app.run(debug=True)
