import dash

from dash import dcc, html, Input, Output, State, dash_table

import pandas as pd

import plotly.express as px

import base64

import io

import requests

import webbrowser

import threading

 

# Automatically open browser when app runs

threading.Timer(1.0, lambda: webbrowser.open("http://127.0.0.1:8050")).start()

 

# Initialize the app with properly formatted external stylesheets

external_stylesheets = ['https://fonts.googleapis.com/css2?family=Segoe+UI:wght@400;600&display=swap']

 

app = dash.Dash(__name__,

               suppress_callback_exceptions=True,

               external_stylesheets=external_stylesheets)

app.title = "Cadmatic Powered Dashboard"

global_df = pd.DataFrame()

 

# Cadmatic logo URL

CADMATIC_LOGO_URL = "https://www.cadmatic.com/assets/themecadmatic/images/logo.svg"

 

# Complete theme styles with all required keys

theme_styles = {

    'dark': {

        'main': {

            'fontFamily': '"Segoe UI", sans-serif',

            'backgroundColor': '#121212',

            'minHeight': '100vh',

            'padding': '20px',

            'color': '#ffffff'

        },

        'header': {

            'display': 'flex',

            'justifyContent': 'space-between',

            'alignItems': 'center',

            'backgroundColor': '#1e1e1e',

            'padding': '16px 24px',

            'borderBottom': '1px solid #333',

            'boxShadow': '0 1px 3px rgba(0,0,0,0.5)'

        },

        'title': {

            'color': '#ffffff',

            'fontSize': '20px',

            'fontWeight': '600',

            'margin': '0'

        },

        'content': {

            'display': 'grid',

            'gridTemplateColumns': '250px 1fr',

            'gap': '20px',

            'marginTop': '20px'

        },

        'sidebar': {

            'backgroundColor': '#1e1e1e',

            'borderRadius': '4px',

            'boxShadow': '0 1px 3px rgba(0,0,0,0.5)',

            'padding': '16px',

            'border': '1px solid #333',

            'color': '#ffffff'

        },

        'main-content': {

            'display': 'flex',

            'flexDirection': 'column',

            'gap': '20px'

        },

        'card': {

            'backgroundColor': '#1e1e1e',

            'borderRadius': '4px',

            'boxShadow': '0 1px 3px rgba(0,0,0,0.5)',

            'padding': '16px',

            'border': '1px solid #333',

            'color': '#ffffff'

        },

        'card-title': {

            'color': '#ffffff',

            'marginTop': '0',

            'fontWeight': '600',

            'fontSize': '18px'

        },

        'upload': {

            'border': '2px dashed #4F46E5',

            'borderRadius': '4px',

            'padding': '40px 20px',

            'textAlign': 'center',

            'cursor': 'pointer',

            'marginBottom': '20px',

            'transition': 'all 0.2s ease',

            ':hover': {

                'borderColor': '#7C73E6'

            }

        },

        'dropdown-container': {

            'display': 'grid',

            'gridTemplateColumns': 'repeat(auto-fit, minmax(200px, 1fr))',

            'gap': '16px',

            'marginBottom': '16px'

        },

        'dropdown': {

            'width': '100%',

            'backgroundColor': '#2d2d2d',

            'color': '#ffffff',

            'border': '1px solid #444',

            'borderRadius': '2px',

            'padding': '8px'

        },

        'button': {

            'backgroundColor': '#4F46E5',

            'color': 'white',

            'border': 'none',

            'padding': '10px 16px',

            'borderRadius': '2px',

            'cursor': 'pointer',

            'fontWeight': '600',

            'transition': 'all 0.2s ease',

            ':hover': {

                'backgroundColor': '#7C73E6'

            }

        },

        'table': {

            'border': '1px solid #333',

            'borderRadius': '4px',

            'overflow': 'hidden'

        },

        'response': {

            'backgroundColor': '#2d2d2d',

            'borderLeft': '4px solid #4F46E5',

            'padding': '16px',

            'borderRadius': '4px',

            'marginTop': '16px',

            'color': '#ffffff'

        },

        'visualization': {

            'border': '1px solid #333',

            'borderRadius': '4px',

            'padding': '16px',

            'height': '500px',

            'backgroundColor': '#1e1e1e'

        },

        'label': {

            'color': '#d4d4d4',

            'marginBottom': '8px',

            'display': 'block',

            'fontWeight': '500'

        },

        'textarea': {

            'width': '100%',

            'minHeight': '100px',

            'padding': '8px',

            'backgroundColor': '#2d2d2d',

            'color': '#ffffff',

            'border': '1px solid #444',

            'borderRadius': '2px',

            'resize': 'vertical'

        },

        'theme-toggle': {

            'backgroundColor': '#333',

            'color': 'white'

        }

    },

    'light': {

        'main': {

            'fontFamily': '"Segoe UI", sans-serif',

            'backgroundColor': '#f5f5f5',

            'minHeight': '100vh',

            'padding': '20px',

            'color': '#333333'

        },

        'header': {

            'display': 'flex',

            'justifyContent': 'space-between',

            'alignItems': 'center',

            'backgroundColor': '#ffffff',

            'padding': '16px 24px',

            'borderBottom': '1px solid #e0e0e0',

            'boxShadow': '0 1px 3px rgba(0,0,0,0.1)'

        },

        'title': {

            'color': '#333333',

            'fontSize': '20px',

            'fontWeight': '600',

            'margin': '0'

        },

        'content': {

            'display': 'grid',

            'gridTemplateColumns': '250px 1fr',

            'gap': '20px',

            'marginTop': '20px'

        },

        'sidebar': {

            'backgroundColor': '#ffffff',

            'borderRadius': '4px',

            'boxShadow': '0 1px 3px rgba(0,0,0,0.1)',

            'padding': '16px',

            'border': '1px solid #e0e0e0',

            'color': '#333333'

        },

        'main-content': {

            'display': 'flex',

            'flexDirection': 'column',

            'gap': '20px'

        },

        'card': {

            'backgroundColor': '#ffffff',

            'borderRadius': '4px',

            'boxShadow': '0 1px 3px rgba(0,0,0,0.1)',

            'padding': '16px',

            'border': '1px solid #e0e0e0',

            'color': '#333333'

        },

        'card-title': {

            'color': '#333333',

            'marginTop': '0',

            'fontWeight': '600',

            'fontSize': '18px'

        },

        'upload': {

            'border': '2px dashed #4F46E5',

            'borderRadius': '4px',

            'padding': '40px 20px',

            'textAlign': 'center',

            'cursor': 'pointer',

            'marginBottom': '20px',

            'transition': 'all 0.2s ease',

            ':hover': {

                'borderColor': '#7C73E6'

            }

        },

        'dropdown-container': {

            'display': 'grid',

            'gridTemplateColumns': 'repeat(auto-fit, minmax(200px, 1fr))',

            'gap': '16px',

            'marginBottom': '16px'

        },

        'dropdown': {

            'width': '100%',

            'backgroundColor': '#ffffff',

            'color': '#333333',

            'border': '1px solid #e0e0e0',

            'borderRadius': '2px',

            'padding': '8px'

        },

        'button': {

            'backgroundColor': '#4F46E5',

            'color': 'white',

            'border': 'none',

            'padding': '10px 16px',

            'borderRadius': '2px',

            'cursor': 'pointer',

            'fontWeight': '600',

            'transition': 'all 0.2s ease',

            ':hover': {

                'backgroundColor': '#7C73E6'

            }

        },

        'table': {

            'border': '1px solid #e0e0e0',

            'borderRadius': '4px',

            'overflow': 'hidden'

        },

        'response': {

            'backgroundColor': '#ffffff',

            'borderLeft': '4px solid #4F46E5',

            'padding': '16px',

            'borderRadius': '4px',

            'marginTop': '16px',

            'color': '#333333'

        },

        'visualization': {

            'border': '1px solid #e0e0e0',

            'borderRadius': '4px',

            'padding': '16px',

            'height': '500px',

            'backgroundColor': '#ffffff'

        },

        'label': {

            'color': '#555555',

            'marginBottom': '8px',

            'display': 'block',

            'fontWeight': '500'

        },

        'textarea': {

            'width': '100%',

            'minHeight': '100px',

            'padding': '8px',

            'backgroundColor': '#ffffff',

            'color': '#333333',

            'border': '1px solid #e0e0e0',

            'borderRadius': '2px',

            'resize': 'vertical'

        },

        'theme-toggle': {

            'backgroundColor': '#e0e0e0',

            'color': '#333333'

        }

    }

}

 

app.layout = html.Div(id='main-container', children=[

    dcc.Store(id='theme-store', data='dark'),

    html.Div(id='dummy-output', style={'display': 'none'}),  # For CSS variables

   

    # Header with Cadmatic logo

    html.Div(id='header', style=theme_styles['dark']['header'], children=[

        html.Div(style={'display': 'flex', 'alignItems': 'center', 'gap': '12px'}, children=[

            html.Img(src=CADMATIC_LOGO_URL,

                    style={'height': '40px', 'objectFit': 'contain'}),

            html.H1("Powered Dashboard", id='title', style=theme_styles['dark']['title']),

        ]),

        html.Div([

            html.Button("Refresh", id='refresh-button', style=theme_styles['dark']['button']),

            html.Button("Export", id='export-button', style={**theme_styles['dark']['button'], 'marginLeft': '8px'}),

            html.Button(

                id='theme-toggle',

                children="☀️ Light Mode",

                style={**theme_styles['dark']['button'], 'marginLeft': '8px'}

            )

        ])

    ]),

   

    # Main Content

    html.Div(id='content', style=theme_styles['dark']['content'], children=[

        # Sidebar

        html.Div(id='sidebar', style=theme_styles['dark']['sidebar'], children=[

            html.H3("Data Sources", style=theme_styles['dark']['card-title']),

            dcc.Upload(

                id='upload-data',

                children=html.Div([

                    html.Div(className="fas fa-cloud-upload", style={'fontSize': '24px', 'color': '#4F46E5'}),

                    html.P("Upload Excel/CSV", style={'marginTop': '8px', 'color': 'inherit'})

                ]),

                style=theme_styles['dark']['upload']

            ),

            html.Div(id='file-info', style={'color': 'inherit', 'marginTop': '10px'}),

            html.H3("Visualization Options", style=theme_styles['dark']['card-title']),

            html.Div(style=theme_styles['dark']['dropdown-container'], children=[

                html.Div([

                    html.Label("Chart Type", style=theme_styles['dark']['label']),

                    dcc.Dropdown(

                        id='chart-type',

                        options=[

                            {'label': 'Bar Chart', 'value': 'bar'},

                            {'label': 'Line Chart', 'value': 'line'},

                            {'label': 'Scatter Plot', 'value': 'scatter'},

                            {'label': 'Pie Chart', 'value': 'pie'},

                            {'label': 'Histogram', 'value': 'histogram'},

                            {'label': 'Area Chart', 'value': 'area'},

                            {'label': 'Box Plot', 'value': 'box'}

                        ],

                        style=theme_styles['dark']['dropdown'],

                        className='dropdown-theme'

                    )

                ]),

                html.Div([

                    html.Label("X-Axis", style=theme_styles['dark']['label']),

                    dcc.Dropdown(id='x-axis', style=theme_styles['dark']['dropdown'], className='dropdown-theme')

                ]),

                html.Div([

                    html.Label("Y-Axis", style=theme_styles['dark']['label']),

                    dcc.Dropdown(id='y-axis', style=theme_styles['dark']['dropdown'], className='dropdown-theme')

                ]),

                html.Div([

                    html.Label("Color", style=theme_styles['dark']['label']),

                    dcc.Dropdown(id='color-axis', style=theme_styles['dark']['dropdown'], className='dropdown-theme')

                ])

            ])

        ]),

       

        # Main Content Area

        html.Div(style=theme_styles['dark']['main-content'], children=[

            # Visualization Card

            html.Div(id='visualization-card', style=theme_styles['dark']['card'], children=[

                html.H3("Visualization", style=theme_styles['dark']['card-title']),

                html.Div(style=theme_styles['dark']['visualization'], children=[

                    dcc.Graph(id='output-graph')

                ])

            ]),

           

            # Data Table Card

            html.Div(id='table-card', style=theme_styles['dark']['card'], children=[

                html.H3("Data Preview", style=theme_styles['dark']['card-title']),

                html.Div(style=theme_styles['dark']['table'], children=[

                    dash_table.DataTable(

                        id='data-table',

                        page_size=10,

                        style_table={'overflowX': 'auto'},

                        style_cell={

                            'padding': '8px',

                            'border': '1px solid',

                            'textAlign': 'left',

                            'backgroundColor': 'inherit',

                            'color': 'inherit'

                        },

                        style_header={

                            'backgroundColor': 'inherit',

                            'fontWeight': '600',

                            'color': 'inherit'

                        },

                        style_data={

                            'border': '1px solid'

                        }

                    )

                ])

            ]),

           

            # AI Assistant Card

            html.Div(id='ai-card', style=theme_styles['dark']['card'], children=[

                html.H3("AI Assistant", style=theme_styles['dark']['card-title']),

                dcc.Textarea(

                    id='user-question',

                    placeholder="Ask questions about your data...",

                    style=theme_styles['dark']['textarea']

                ),

                html.Button("Ask AI", id='ask-button', style={**theme_styles['dark']['button'], 'marginTop': '12px'}),

                dcc.Loading(

                    id="loading-llama",

                    type="default",

                    children=html.Div(id='chatbot-response', style=theme_styles['dark']['response'])

                )

            ])

        ])

    ])

])

 

# Clientside callback for CSS variables

app.clientside_callback(

    """

    function(theme) {

        const styles = {

            dark: {

                '--dropdown-bg': '#2d2d2d',

                '--dropdown-text': '#ffffff',

                '--dropdown-border': '#444'

            },

            light: {

                '--dropdown-bg': '#ffffff',

                '--dropdown-text': '#333333',

                '--dropdown-border': '#e0e0e0'

            }

        };

       

        const selected = theme === 'dark' ? styles.dark : styles.light;

        for (const [key, value] of Object.entries(selected)) {

            document.documentElement.style.setProperty(key, value);

        }

        return window.dash_clientside.no_update;

    }

    """,

    Output('dummy-output', 'children'),

    Input('theme-store', 'data')

)

 

# Theme toggle callback

@app.callback(

    Output('theme-store', 'data'),

    Input('theme-toggle', 'n_clicks'),

    State('theme-store', 'data')

)

def toggle_theme(n_clicks, current_theme):

    if n_clicks is None:

        return current_theme

    return 'light' if current_theme == 'dark' else 'dark'

 

# Update all components based on theme

@app.callback(

    Output('main-container', 'style'),

    Output('header', 'style'),

    Output('title', 'style'),

    Output('sidebar', 'style'),

    Output('visualization-card', 'style'),

    Output('table-card', 'style'),

    Output('ai-card', 'style'),

    Output('upload-data', 'style'),

    Output('file-info', 'style'),

    Output('theme-toggle', 'children'),

    Output('theme-toggle', 'style'),

    Output('chart-type', 'style'),

    Output('x-axis', 'style'),

    Output('y-axis', 'style'),

    Output('color-axis', 'style'),

    Input('theme-store', 'data')

)

def update_theme(theme):

    styles = theme_styles[theme]

    button_text = "🌙 Dark Mode" if theme == 'light' else "☀️ Light Mode"

   

    return (

        styles['main'],

        styles['header'],

        styles['title'],

        styles['sidebar'],

        styles['card'],

        styles['card'],

        styles['card'],

        styles['upload'],

        {'color': 'inherit'},

        button_text,

        styles['button'],

        styles['dropdown'],

        styles['dropdown'],

        styles['dropdown'],

        styles['dropdown']

    )

 

# File upload callback

@app.callback(

    Output('file-info', 'children'),

    Output('x-axis', 'options'),

    Output('y-axis', 'options'),

    Output('color-axis', 'options'),

    Output('data-table', 'columns'),

    Output('data-table', 'data'),

    Input('upload-data', 'contents'),

    State('upload-data', 'filename')

)

def handle_upload(contents, filename):

    if contents is None:

        return "", [], [], [], [], []

 

    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)

    try:

        if filename.endswith('.csv'):

            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))

        else:

            df = pd.read_excel(io.BytesIO(decoded), engine='openpyxl')

    except Exception as e:

        return f"❌ Error: {e}", [], [], [], [], []

 

    df.columns = [f"Column {i+1}" if str(col).startswith("Unnamed") else str(col) for i, col in enumerate(df.columns)]

 

    global global_df

    global_df = df

 

    options = [{'label': col, 'value': col} for col in df.columns]

    columns = [{'name': col, 'id': col} for col in df.columns]

    return f"✅ Uploaded: {filename}", options, options, options, columns, df.head(100).to_dict('records')

 

# Graph update callback

@app.callback(

    Output('output-graph', 'figure'),

    Input('chart-type', 'value'),

    Input('x-axis', 'value'),

    Input('y-axis', 'value'),

    Input('color-axis', 'value')

)

def update_graph(chart_type, x_col, y_col, color_col):

    if not chart_type or not x_col:

        return {}

    df = global_df

    try:

        if chart_type == 'bar':

            fig = px.bar(df, x=x_col, y=y_col, color=color_col, barmode='group')

        elif chart_type == 'line':

            fig = px.line(df, x=x_col, y=y_col, color=color_col)

        elif chart_type == 'scatter':

            fig = px.scatter(df, x=x_col, y=y_col, color=color_col)

        elif chart_type == 'pie':

            fig = px.pie(df, names=x_col, values=y_col, color=color_col)

        elif chart_type == 'histogram':

            fig = px.histogram(df, x=x_col, color=color_col)

        elif chart_type == 'area':

            fig = px.area(df, x=x_col, y=y_col, color=color_col)

        elif chart_type == 'box':

            fig = px.box(df, x=x_col, y=y_col, color=color_col)

       

        # Theme for plots

        current_theme = dash.callback_context.inputs.get('theme-store.data', 'dark')

        if current_theme == 'dark':

            fig.update_layout(

                plot_bgcolor='#1e1e1e',

                paper_bgcolor='#1e1e1e',

                font={'family': '"Segoe UI", sans-serif', 'color': 'white'},

                margin={'l': 40, 'b': 40, 't': 40, 'r': 40},

                xaxis={'gridcolor': '#333'},

                yaxis={'gridcolor': '#333'},

                legend={'bgcolor': '#1e1e1e'}

            )

        else:

            fig.update_layout(

                plot_bgcolor='#ffffff',

                paper_bgcolor='#ffffff',

                font={'family': '"Segoe UI", sans-serif', 'color': '#333333'},

                margin={'l': 40, 'b': 40, 't': 40, 'r': 40},

                xaxis={'gridcolor': '#e0e0e0'},

                yaxis={'gridcolor': '#e0e0e0'},

                legend={'bgcolor': '#ffffff'}

            )

        return fig

    except Exception as e:

        print(f"Error creating figure: {e}")

        return {}

 

# Chatbot callback

@app.callback(

    Output('chatbot-response', 'children'),

    Input('ask-button', 'n_clicks'),

    State('user-question', 'value')

)

def query_chatbot(n, question):

    if not n or not question or global_df.empty:

        return ""

    try:

        info = f"Shape: {global_df.shape}, Columns: {list(global_df.columns)}\n\nSample:\n{global_df.head(2).to_string(index=False)}"

        prompt = f"You are a helpful AI. Dataset:\n{info}\n\nUser question: {question}"

 

        response = requests.post("http://localhost:11434/api/generate",

                               json={"model": "llama3", "prompt": prompt, "stream": False})

        if response.status_code == 200:

            return response.json().get("response", "")

        else:

            return f"Error {response.status_code} from Ollama"

    except Exception as e:

        return f"❌ AI Error: {e}"

 

if __name__ == '__main__':

    app.run(debug=True)