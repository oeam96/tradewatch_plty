#THIS APPLICATION IS BASED ON THE ONE PUBLISHED BY TANYA LOMSKAYA WHICH IS PART OF THE "DASH EXAMPLE GALLERY"
#Link will be provided after

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

#Launching the Application
app = Dash(__name__)

#Main Layout
app.layout = dbc.Container(html.P("My Dashboard"),
                            fluid=True)

#Runnin the app with development server in debug mode
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
