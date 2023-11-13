import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np
from dash.exceptions import PreventUpdate
import recursos as r

# Crear la aplicación Dash
app = dash.Dash(__name__)

# Datos de ejemplo para las gráficas
x = np.linspace(0, 10, 1000)
global c
c=0
ruta=".venv\BaseDatos_EMG_Acc-20230304T150927Z-001\BaseDatos_EMG_Acc"

n=110000
f=1000
t = np.linspace(0, n / f, n)
data=[]
data_sm=[]
# Estructura de datos compartida para almacenar los datos de las gráficas
data_store = {
    'y1': data,
    'y2': data_sm,
    'y3': data[0:1000],
    'y4': data[0:1000],
    'y5': data[0:1000],
    'y6': data[0:1000]
}

# Diseño de la aplicación
app.layout = html.Div([
    dcc.Graph(id='graph-1', style={'width': '100%', 'display': 'inline-block', 'verticalAlign': 'top'}),
    dcc.Graph(id='graph-2', style={'width': '100%', 'display': 'inline-block', 'verticalAlign': 'top'}),
    dcc.Graph(id='graph-3', style={'width': '25%', 'display': 'inline-block', 'verticalAlign': 'top'}),
    dcc.Graph(id='graph-4', style={'width': '25%', 'display': 'inline-block', 'verticalAlign': 'top'}),
    dcc.Graph(id='graph-5', style={'width': '25%', 'display': 'inline-block', 'verticalAlign': 'top'}),
    dcc.Graph(id='graph-6', style={'width': '25%', 'display': 'inline-block', 'verticalAlign': 'top'}),
    dcc.Interval(
        id='interval-component',
        interval=5000,  # en milisegundos
        n_intervals=0
    ),
])


# Callbacks para actualizar los gráficos en tiempo real
@app.callback(
    [Output('graph-1', 'figure'),
     Output('graph-2', 'figure'),
     Output('graph-3', 'figure'),
     Output('graph-4', 'figure'),
     Output('graph-5', 'figure'),
     Output('graph-6', 'figure')],
    Input('interval-component', 'n_intervals'),
)

def update_graph(n):
    data=r.LR_file(np.random.randint(10),ruta)
    data_sm=r.suavizar(r.envolvente(data),1000,3)
   
    ctx = dash.callback_context
      


    if not ctx.triggered_id:
        raise PreventUpdate

    # Actualizar los datos según sea necesario
    data_store['y1'] = data
    data_store['y2'] = data_sm
    data_store['y3'] = data[0:1000]
    data_store['y4'] = data[0:1000]
    data_store['y5'] = data[0:1000]
    data_store['y6'] = data[0:1000]

    # Crear figuras de Plotly actualizadas
    indicator=['Fatiga', 'No fatiga']
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=t, y=data_store['y1'], mode='lines'))
    fig1.update_layout(title='EMG signal')

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=t, y=data_store['y2'], mode='lines'))
    fig2.update_layout(title='EMG signal (Envelope)')

    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=t[0:1000], y=data_store['y3'], mode='lines'))
    fig3.update_layout(title=f'Segmento 1 [{indicator[0]}]')

    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(x=t[0:1000], y=data_store['y4'], mode='lines'))
    fig4.update_layout(title=f'Segmento 2 [{indicator[1]}]')

    fig5 = go.Figure()
    fig5.add_trace(go.Scatter(x=t[0:1000], y=data_store['y5'], mode='lines'))
    fig5.update_layout(title=f'Segmento 3 [{indicator[0]}]')
    
    fig6 = go.Figure()
    fig6.add_trace(go.Scatter(x=t[0:1000], y=data_store['y6'], mode='lines'))
    fig6.update_layout(title=f'Segmento 4 [{indicator[1]}]')

    return fig1, fig2, fig3, fig4, fig5, fig6

if __name__ == '__main__':
    app.run_server(debug=False)
