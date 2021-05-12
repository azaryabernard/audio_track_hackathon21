import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

#create dataframes & function
dfrow1 = pd.read_csv('speechrecog\dfrow1.csv')
dfrow2 = pd.read_csv('speechrecog\dfrow2.csv')

def command_light(bool_light, color, speech):
    if bool_light == True:
        dfrow1.loc[0,'Light'] = color
    dfrow1.loc[1,'Light'] = speech
    dfrow1.to_csv('dfrow1.csv', index=False)

def command_SoundSystem(command, volume, speech):
    text_df = f"{command}, Vol: {volume}%"
    dfrow1.loc[0,['SoundSystem']] = text_df
    dfrow1.loc[1,['SoundSystem']] = speech
    dfrow1.to_csv('dfrow1.csv', index=False)

def command_Door(open_or_close, speech):
    dfrow1.loc[0,['Door']] = f"Door is {open_or_close}"
    dfrow1.loc[1,['Door']] = speech
    dfrow1.to_csv('dfrow1.csv', index=False)

def command_detectsound(label):
    if label == "air_conditioner":
        dfrow2.loc[1,['InfoDetectSound']] = "Your air conditioner seems to be on.."
    if label == "car_horn":
        dfrow2.loc[1,['InfoDetectSound']] = "Someone is honking.. do you have a guest in front?"
    if label == "children_playing":
        dfrow2.loc[1,['InfoDetectSound']] = "Your children are having fun"
    if label == "dog_bark":
        dfrow2.loc[1,['InfoDetectSound']] = "Your dog is barking.. is someone breaking in?"
    if label == "drilling":
        dfrow2.loc[1,['InfoDetectSound']] = "Someone is drilling... a robber??"
    if label == "engine_idling":
        dfrow2.loc[1,['InfoDetectSound']] = "Did you maybe forget to turn off your car?"
    if label == "gun_shot":
        dfrow2.loc[1,['InfoDetectSound']] = "Call the police, someone shot a gun!!"
    if label == "jackhammer":
        dfrow2.loc[1,['InfoDetectSound']] = "Jackhammer.. any construction going on??"
    if label == "siren":
        dfrow2.loc[1,['InfoDetectSound']] = "There is siren, check what's going on!!"
    if label == "street_music":
        dfrow2.loc[1,['InfoDetectSound']] = "Some street music! Open your window to enjoy.. "
    dfrow2.loc[0,['InfoDetectSound']] = label
    dfrow2.to_csv('dfrow2.csv', index=False)

def create_dashboard():
    dfrow1 = pd.read_csv('dfrow1.csv')
    dfrow2 = pd.read_csv('dfrow2.csv')
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

        html.Div(style={'backgroundColor': colors['commandbackground'], 'marginLeft': 250, 'marginRight': 250, 'marginBottom': 50}, children =[
            html.P(style={'font-size': 17,'textAlign': 'center', 'color': colors['text']}, children=[
                'Here is a list of available commands for your smart home:', 
                html.Br(),
                html.Br(),
                'Lights on / Lights off',
                html.Br(),
                'Set Lights Brightness & Color',
                html.Br(),
                'Play a Song / Pause a Song / Stop a Song',
                html.Br(),
                'Volume Up / Volume Down',
                html.Br(),
                'Open the door / Close the door'
            ]),
            html.Div(style={'backgroundColor':'#FFFFFF', 'marginLeft': 250, 'marginRight': 250}, children=[
                html.P(style={'font-size': 17,'textAlign': 'center', 'color': '#e12120'}, children=[
                    'Detect Sound'
                ])
            ])
        ]),

        # first row (title)
        html.Div(children=[

            # first column of first row
            html.Div(children=[
                html.H3(children='Light',
                    style={
                        'textAlign': 'center',
                        'color': colors['text']
                    }
                )
            ], style={'width':'31%', 'display': 'inline-block', 'vertical-align': 'top', 'margin-top': '3vw', 'margin-bottom': '0'}),

            # second column of first row
            html.Div(children=[
                html.H3(children='Sound System',
                    style={
                        'textAlign': 'center',
                        'color': colors['text']
                    }
                )
            ], style={'width':'31%', 'display': 'inline-block', 'vertical-align': 'top', 'margin-top': '3vw', 'margin-bottom': '0', 'margin-left': '3vw'}),

            # third column of first row
            html.Div(children=[
                html.H3(children='Door',
                    style={
                        'textAlign': 'center',
                        'color': colors['text']
                    }
                )
            ], style={'width':'31%', 'display': 'inline-block', 'vertical-align': 'top', 'margin-top': '3vw', 'margin-bottom': '0',  'margin-left': '3vw'}),

        ], className='row'),   

        dash_table.DataTable(
            data=dfrow1.to_dict('records'),
            columns=[
                {'name': 'Light', 'id': 'Light', 'type': 'text'},
                {'name': 'SoundSystem', 'id': 'SoundSystem', 'type': 'text'},
                {'name': 'Door', 'id': 'Door', 'type': 'text'},
            ],
            style_header={'display': 'none'},
            style_cell = {
                    'whiteSpace': 'normal',
                    'font_size': '15px',
                    'text_align': 'center',
                    'width': '33%',
                    'backgroundColor': '#000000',
                    'color': '#FFFFFF',
                    'height': 'auto',
                },
            cell_selectable=False,
            style_data_conditional=[
                {
                    'if': {
                        'row_index': 0,
                        'column_id': 'Light',
                    },
                    'backgroundColor': dfrow1.iloc[0]['Light']
                }

            ]  
        ),

        # second row (title)
        html.Div(children=[

            # only column of second row
            html.Div(children=[
                html.H3(children='Information from your House',
                    style={
                        'textAlign': 'center',
                        'color': colors['text']
                    }
                )
            ], style={'width':'100%', 'display': 'inline-block', 'vertical-align': 'top', 'margin-top': '5vw', 'margin-bottom': '0'}),

        ], className='row'),   

        dash_table.DataTable(
            data=dfrow2.to_dict('records'),
            columns=[
                {'name': 'Information Detect Sound', 'id': 'InfoDetectSound', 'type': 'text'},
            ],
            style_header={'display': 'none'},
            style_cell = {
                    'whiteSpace': 'normal',
                    'font_size': '15px',
                    'text_align': 'center',
                    'width': '100%',
                    'backgroundColor': '#000000',
                    'color': '#FFFFFF',
                    'height': 'auto',
                },
            cell_selectable=False
        ) 

        
    ])
    return app

def run_dash():
    app.run_server(debug=True)

if __name__ == '__main__':
    app.run_server(debug=True)
