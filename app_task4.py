import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.graph_objects as go

# Load and prepare data
df = pd.read_csv('Formated_Output.csv')
df['date'] = pd.to_datetime(df['date'])
df.sort_values(by='date', inplace=True)

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Soul Foods Sales Dashboard"

# App layout
app.layout = html.Div([
    html.H1("Soul Foods Sales Visualizer", style={
        'textAlign': 'center',
        'color': '#2c3e50',
        'font-family': 'Verdana',
        'margin-bottom': '0'
    }),

    html.P("Sales before and after Pink Morsel price increase on Jan 15, 2021", style={
        'textAlign': 'center',
        'fontSize': '18px',
        'color': '#34495e',
        'margin-top': '0',
        'margin-bottom': '30px'
    }),

    html.Div([
        html.Label("Select Region:", style={
            'fontSize': '18px',
            'fontWeight': 'bold',
            'color': '#2c3e50'
        }),
        dcc.RadioItems(
            id='region-selector',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'}
            ],
            value='all',
            inline=True,
            labelStyle={'padding': '10px', 'fontSize': '16px'}
        )
    ], style={'textAlign': 'center', 'margin-bottom': '30px'}),

    dcc.Graph(id='sales-graph')
], style={'padding': '20px', 'backgroundColor': '#ecf0f1'})


# Callback to update graph based on region
@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-selector', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'].str.lower() == selected_region]

    daily_sales = filtered_df.groupby('date', as_index=False)['Sales'].sum()

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=daily_sales['date'],
        y=daily_sales['Sales'],
        mode='lines+markers',
        name='Total Sales',
        line=dict(color='#2980b9')
    ))

    # Add vertical line on Jan 15, 2021
    fig.add_vline(x='2021-01-15', line_width=4, line_dash='dash', line_color='red')
    fig.add_annotation(x='2021-01-15', y=daily_sales['Sales'].max() if not daily_sales.empty else 0,
                       text='Price Increase', showarrow=True, arrowhead=1)

    fig.update_layout(
        title=f"Total Sales Over Time ({selected_region.capitalize() if selected_region != 'all' else 'All Regions'})",
        xaxis_title='Date',
        yaxis_title='Total Sales ($)',
        template='plotly_white',
        plot_bgcolor='#ffffff',
        font=dict(family='Verdana', size=14, color='#2c3e50')
    )

    return fig


# Run server
if __name__ == '__main__':
    app.run(debug=True)
