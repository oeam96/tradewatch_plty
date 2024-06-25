#THIS APPLICATION IS BASED ON THE ONE PUBLISHED BY TANYA LOMSKAYA WHICH IS PART OF THE "DASH EXAMPLE GALLERY"
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
app.layout = dbc.Container([html.Div(), html.Div()],
                            fluid=True,
                            className="dashboard-container")

#Runnin the app with development server in debug mode
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
