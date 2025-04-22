
import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd

df_metrics = pd.read_csv("df_metrics.csv")  # <- você precisa salvar esse CSV também

COLUNA_LABEL = 'label'
colunas = df_metrics.columns.tolist()
colunas.remove(COLUNA_LABEL)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Boxplot"),
    dcc.Dropdown(
        id='coluna-dropdown',
        options=[{'label': col, 'value': col} for col in colunas],
        value=colunas[0],
        clearable=False,
        style={'width': '300px'}
    ),
    dcc.Graph(id='boxplot-graph')
])

@app.callback(
    Output('boxplot-graph', 'figure'),
    Input('coluna-dropdown', 'value')
)
def atualizar_boxplot(coluna_escolhida):
    fig = px.box(
        df_metrics,
        x=COLUNA_LABEL,
        y=coluna_escolhida,
        color=COLUNA_LABEL,
        color_discrete_map={0: "blue", 1: "red"},
        labels={COLUNA_LABEL: "Classe", coluna_escolhida: coluna_escolhida},
        title=f"Distribuição da coluna '{coluna_escolhida}' por classe"
    )
    return fig

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    