# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from django_plotly_dash import DjangoDash
import pandas as pd
from dash.dependencies import Input, Output
from django.conf import settings

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('DashPlot1', external_stylesheets=external_stylesheets)
#app = dash.Dash(__name__)

file_name = settings.MEDIA_ROOT + "/thermistorK.txt"
data = pd.read_csv(file_name, 
    sep = " ", header=None, names=["time","thermistor", "value"])

#print(data.info())

available_indicators = data['thermistor'].unique()

app.layout = html.Div(children=[
    #html.H1(children='IFE Dashboard'),

    #html.Div(children='''
    #    Created using Dash: A web application framework for Python.
    #'''),

    dcc.Graph(id='example-graph'),
    
    html.Div([
        dcc.Dropdown(
            id='thermistor-num',
            options=[{'label': i, 'value': i} for i in available_indicators],
            value="thermistor number",
            multi=True,
            placeholder="Select a thermistor number"
        )
    ]),
])


@app.callback(
    Output('example-graph', 'figure'),
    [Input('thermistor-num', 'value')])
def update_figure(thermistor_value):
    traces = []
    for i in thermistor_value:
        traces.append(dict(
            x=data[data['thermistor'] == i]['time'],
            y=data[data['thermistor'] == i]['value'],
            text=data[data['thermistor'] == i]['thermistor'],
            mode = 'markers',
            opacity=0.7,
            marker={
                'size': 5,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
         ))
    return {
        'data': traces,
        'layout': dict(
            xaxis={'title':'Time(s)'},
            yaxis={'title':'ADC Bits'},
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)