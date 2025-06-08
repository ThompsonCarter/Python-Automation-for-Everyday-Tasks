
import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/monthly_sales.csv")

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Sales Dashboard"),
    dcc.Dropdown(
        id="region-dropdown",
        options=[{"label": r, "value": r} for r in df["region"].unique()],
        value=df["region"].unique()[0]
    ),
    dcc.Graph(id="sales-graph")
])

@app.callback(
    dash.dependencies.Output("sales-graph", "figure"),
    [dash.dependencies.Input("region-dropdown", "value")]
)
def update_graph(region):
    filtered = df[df["region"] == region]
    fig = px.line(filtered, x="month", y="amount", title=f"Sales in {region}")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
