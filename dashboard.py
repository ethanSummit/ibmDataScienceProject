import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('')


# Initialize the Dash app
app = dash.Dash(__name__)

# List of years
year_list = [i for i in range(1980, 2024, 1)]

# Create the layout of the app
app.layout = html.Div([
    html.H1("Automobile Sales Statistics Dashboard",
            style={'textAlign': 'center', 'color': 'red', 'font-size' : 24}),
    html.Div([
        html.Div(
            html.Label("Select Statistics:",
                   style={ 'color': 'blue','font-weight': 'bold','font': '14px Arial, Helvetica, sans-serif'}
                   ),
            style={'width': '60%','height':'24px','margin-left':'48px','padding':'15px'}

        ),

        dcc.Dropdown(
            id='select-statistics',
            options=[
                {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
                {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
            ],
            value='Yearly Statistics',
            placeholder='Select Statistics',
            style={
    'font-weight': 'bold',
    'font': '18px Arial, Helvetica, sans-serif'}
        )
    ]),
    html.Div(dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            value=1980
        )),
    html.Div([
        html.Div(id='output-container', className='output-container', style={'width': '100%','margin':'auto', 'display': 'inline-block'}),
    ])
])

@app.callback(
    Output(component_id='select-year', component_property='disabled'),
    Input(component_id='select-statistics', component_property='value'))
def update_input_container(selected_statistics):
    if selected_statistics == 'Yearly Statistics':
        return False
    else:
        return True

@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='select-statistics', component_property='value'),
    Input(component_id='select-year', component_property='value')])
def update_output_container(selected_statistics, input_year):
    if selected_statistics == 'Recession Period Statistics':
        recession_data = data[data['Recession'] == 1]

        # Example plot: Change this according to your specific needs
        plot1 = px.line(recession_data, x='Year', y='Automobile_Sales', title='Automobile Sales Over the Years During Recession')

        return [
            dcc.Graph(figure=plot1)
        ]
    elif input_year and selected_statistics == 'Yearly Statistics':
        yearly_data = data[data['Year'] == input_year]

        # Example plot: Change this according to your specific needs
        plot2 = px.bar(yearly_data, x='Month', y='Automobile_Sales', title=f'Automobile Sales in {input_year}')

        return [
            dcc.Graph(figure=plot2)
        ]
    else:
        return None

if __name__ == '__main__':
    app.run_server(mode='inline')