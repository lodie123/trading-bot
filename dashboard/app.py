import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Trading Bot Dashboard"),
    dcc.Interval(id='interval', interval=5000, n_intervals=0),
    dcc.Graph(id='price-graph')
])

@app.callback(
    dash.dependencies.Output('price-graph', 'figure'),
    [dash.dependencies.Input('interval', 'n_intervals')]
)
def update_graph(n):
    try:
        df = pd.read_csv("trades.log", sep=" ", header=None, names=["action", "amount", "x", "price"])
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=df["price"], mode='lines+markers'))
        return fig
    except:
        return go.Figure()

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8050)
