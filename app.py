#THIS APPLICATION IS BASED ON THE ONE PUBLISHED BY TANYA LOMSKAYA
#WHICH IS PART OF THE "DASH EXAMPLE GALLERY"
#Link will be provided after

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

external_stylesheets = [
    'https://fonts.googleapis.com/css2?family=Poppins&display=swap',
     dbc.themes.FLATLY
]

#Launching the Application
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.css.config.serve_locally = True

#Main Layout
app.layout = dbc.Container([
        html.Div([
                html.Div([
                    html.H1([
                        html.Span("Welcome"),
                        html.Span("to the Dashboard Demo")
                    ]),
                    html.P("This is a demo in construction that will display trade data")
                ],
                    style={
                        "vertical-alignment": "top",
                        "height": 260
                    }
                ),
                html.Div(),
                html.Div(),
                html.Div()
        ],
        style={
        'width': 340,
        'margin-left': 35,
        'margin-top': 35,
        'margin-bottom': 35,
    }),
    html.Div(
        [html.Div(style={'width': 790}),
         html.Div(style={'width': 200})],
        style={
        'width': 990,
        'margin-top': 35,
        'margin-right': 35,
        'margin-bottom': 35,
        'display': 'flex'
    })
],
    fluid=True,
    className="dashboard-container")

#Runnin the app with development server in debug mode
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
