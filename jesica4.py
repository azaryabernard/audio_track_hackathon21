import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.BOOTSTRAP]

colors = {
    'background': '#111111',
    'text': '#FFFFFF',
    'commandtext': '#7FDBFF',
    'commandbackground': '#1287A8'
}


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(style={'backgroundColor': colors['background'], 'padding':50}, children=[
    html.H1(children='Hello, Welcome to your Smart Home!',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(style={'backgroundColor': colors['commandbackground'], 'marginLeft': 250, 'marginRight': 250}, children =[
        html.P(style={'font-size': 17,'textAlign': 'center', 'color': colors['text']}, children=[
            'Here is a list of available commands for your smart home:', 
            html.Br(),
            html.Br(),
            'Lights on / Lights off',
            html.Br(),
            'Play a Song / Stop a Song',
            html.Br(),
            'Volume Up / Volume Down',
            html.Br(),
            'Open the door / Close the door',
            html.Br(),
            'Make it Colder / Make it Warmer'
        ])
    ]),

    # first row (title)
    html.Div(children=[

        # first column of first row
        html.Div(children=[
            html.H1(children='Light',
                style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
            )
        ], style={'width':'30%', 'display': 'inline-block', 'vertical-align': 'top', 'margin-top': '3vw'}),

        # second column of first row
        html.Div(children=[
            html.H1(children='Sound System',
                style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
            )
        ], style={'width':'30%', 'display': 'inline-block', 'vertical-align': 'top', 'margin-top': '3vw', 'margin-left': '3vw'}),

        # third column of first row
        html.Div(children=[
            html.H1(children='Door',
                style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
            )
        ], style={'width':'30%', 'display': 'inline-block', 'vertical-align': 'top', 'margin-top': '3vw', 'margin-left': '3vw'}),

    ], className='row'),

    # first row (content)
    html.Div(children=[
            
        # first column of first row
        html.Div(children=[
            dcc.RadioItems(id = 'radio-item-1',
                           options = [dict(label = 'option A', value = 'A'),
                                      dict(label = 'option B', value = 'B'),
                                      dict(label = 'option C', value = 'C')],
                            value = 'A',
                            labelStyle={'display': 'block'}),
            html.P(id = 'text-1',
                   children = 'First paragraph'),
        ], style={'width':'30%', 'backgroundColor': colors['commandbackground'], 'display': 'inline-block', 'vertical-align': 'top', 'margin-top': '3vw'}),

        # second column of first row
        html.Div(children=[
            dcc.RadioItems(id = 'radio-item-2',
                       options = [dict(label = 'option 1', value = '1'),
                                  dict(label = 'option 2', value = '2'),
                                  dict(label = 'option 3', value = '3')],
                       value = '1',
                       labelStyle={'display': 'block'}),
            html.P(id='text-2',
                   children='Second paragraph'),
        ], style={'width':'30%', 'backgroundColor': colors['commandbackground'], 'display': 'inline-block', 'vertical-align': 'top', 'margin-top': '3vw', 'margin-left': '3vw'}),

        # third column of first row
        html.Div(children=[

            #html.Div(dcc.Graph(id = 'main-graph',
            #                   figure = figure)),
            'tes'

        ], style={'width':'30%', 'backgroundColor': colors['commandbackground'], 'display': 'inline-block', 'vertical-align': 'top', 'margin-top': '3vw', 'margin-left': '3vw'}),
    ], className='row'),

    # second row
    html.Div(children=[
        'tes juga'
        #html.Div(dash_table.DataTable(id = 'main-table',
        #                              columns = [{"name": i, "id": i} for i in df.columns],
        #                              data = df.to_dict('records'),
        #                              style_table={'margin-left': '3vw', 'margin-top': '3vw'})),
    ], style={'marginTop': 50, 'width':'70%', 'backgroundColor': colors['commandbackground']}, className='row'),

    
])

if __name__ == '__main__':
    app.run_server(debug=True)