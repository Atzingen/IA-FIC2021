from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('titanic/train.csv')

fig1 = px.parallel_categories(df)
fig2 = px.violin(df, y='Age')

app.layout = html.Div([
    html.H1("Olá Curso de IA !"),
    html.P("descrição do meu super gráfico !"),
    dcc.Graph(id='graph1', figure=fig1),
    html.H1("E agora um gráfico de Violino ..."),
    dcc.Graph(id='graph2', figure=fig2),
    dcc.Dropdown(id='dropdown1', options=[
        {'label': 'Age', 'value': 'Age'},
        {'label': 'Sex', 'value': 'Sex'},
    ])
])

# @app.callback(
#     Output(component_id='dropdown1', component_property='children'),
#     Input(component_id='graph2', component_property='value')
# )
# def get_data(value):
#     px.violin(df, y=value)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8000, debug=True)