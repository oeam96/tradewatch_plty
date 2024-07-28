#THIS APPLICATION IS BASED ON THE ONE PUBLISHED BY TANYA LOMSKAYA
#WHICH IS PART OF THE "DASH EXAMPLE GALLERY"
#Link will be provided after

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import numpy as np
import random

external_stylesheets = [
    'https://fonts.googleapis.com/css2?family=Poppins&display=swap',
     dbc.themes.FLATLY
]

#Launching the Application
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.css.config.serve_locally = True

fig = go.Figure(
    go.Scattergl(
        x = np.random.randn(1000),
        y = np.random.randn(1000),
        mode='markers',
        marker=dict(
            color=random.sample(['#ecf0f1'] * 500 +
                                ['#3498db'] * 500, 1000),
            line_width=1)
    ))

fig.update_layout(plot_bgcolor='#010103',
                  width=790,
                  height=730,
                  xaxis_visible=False,
                  yaxis_visible=False,
                  showlegend=False,
                  margin=dict(l=0, r=0, t=0, b=0))

#Main Layout
app.layout = dbc.Container([
        html.Div([
                html.Div([
                    html.H1([
                        html.Span("Welcome"),
                        html.Br(),
                        html.Span("to the Dashboard Demo")
                    ]),
                    html.P("This is a demo in construction that will display trade data")
                ],
                    style={
                        "vertical-alignment": "top",
                        "height": 260
                    }
                ),
                html.Div(
                    [
                        html.Div(dbc.RadioItems(
                            className='btn-group',
                            inputClassName='btn-check',
                            labelClassName='btn btn-outline-light',
                            labelCheckedClassName='btn btn-light',
                            options=[
                                {"label": "Graph", "value": 1},
                                {"label": "Table", "value": 2}
                            ],
                            value = 1,
                            style={'width': '100%'}
                        ),
                                 style={'width': 206}),
                        html.Div(dbc.Button(
                            "About",
                            className="btn btn-info",
                            n_clicks=0
                        ),
                                style={'width': 104})
                    ],
                    style={
                        'margin-left': 15,
                        'margin-right': 15,
                        'display': 'flex'
                    }),
                html.Div([
                    html.Div([html.H2('Unclearable Dropdown:'),
                              dcc.Dropdown(
                                  className='customDropdown',
                                  options=[
                                      {'label': 'Option A', 'value': 1},
                                      {'label': 'Option B', 'value': 2},
                                      {'label': 'Option C', 'value': 3}
                                  ],
                                  value=1,
                                  clearable=False,
                                  optionHeight=40
                              )
                    ]),
                    html.Div([html.H2('Unclearable Dropdown:'),
                              dcc.Dropdown(
                                  className='customDropdown',
                                  options=[
                                      {'label': 'Option A', 'value': 1},
                                      {'label': 'Option B', 'value': 2},
                                      {'label': 'Option C', 'value': 3}
                                  ],
                                  value=2,
                                  clearable=False,
                                  optionHeight=40
                              )
                    ]),
                    html.Div([html.H2('Unclearable Dropdown:'),
                              dcc.Dropdown(
                                  className='customDropdown',
                                  options=[
                                      {'label': 'Option A', 'value': 1},
                                      {'label': 'Option B', 'value': 2},
                                      {'label': 'Option C', 'value': 3}
                                  ],
                                  clearable=True,
                                  optionHeight=40
                              )
                    ])
                ],
                    style={
                        'margin-left': 15,
                        'margin-right': 15,
                        'margin-top': 30
                    }),
                html.Div(
                    html.Img(src='assets/image.svg',
                             style={
                                 'margin-left': 15,
                                 'margin-right': 15,
                                 'margin-top': 30,
                                 'width': 310
                             })
                )
        ],
        style={
        'width': 340,
        'margin-left': 35,
        'margin-top': 35,
        'margin-bottom': 35,
    }),
    html.Div(
        [html.Div(dcc.Graph(figure=fig), style={'width': 790}),
         html.Div([
            html.H2('Output 1:'),
            html.Div(className='Output'),
            html.H2('Output 2:'),
            html.Div(html.H3('Selected value'), className='Output') 
         ],
            style={'width': 200})],
        style={
        'width': 990,
        'margin-top': 35,
        'margin-right': 35,
        'margin-bottom': 35,
        'display': 'flex'
    })
],
    fluid=True,
    style={'display': 'flex'},
    className="dashboard-container")

#Runnin the app with development server in debug mode
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
