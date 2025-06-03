import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load and prepare data
df = pd.read_csv('Formated_Output.csv')

# Ensure 'date' is in datetime format and sort it
df['date'] = pd.to_datetime(df['date'])
df.sort_values(by='date', inplace=True)

# Group by date to get total sales per day
daily_sales = df.groupby('date', as_index=False)['Sales'].sum()

# Create the figure with a vertical line on Jan 15, 2021
fig = go.Figure()

# Add line chart of total sales
fig.add_trace(go.Scatter(
    x=daily_sales['date'],
    y=daily_sales['Sales'],
    mode='lines+markers',
    name='Total Sales',
    line=dict(color='blue')
))

# Add vertical line for Jan 15, 2021
fig.add_vline(x='2021-01-15', line_width=2, line_dash='dash', line_color='red')
fig.add_annotation(x='2021-01-15', y=max(daily_sales['Sales']),
                   text='Price Increase', showarrow=True, arrowhead=1)

# Customize layout
fig.update_layout(
    title='Total Sales Over Time',
    xaxis_title='Date',
    yaxis_title='Total Sales ($)',
    template='plotly_white'
)

# Initialize Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Soul Foods Sales Visualizer", style={'textAlign': 'center'}),
    html.P("Sales before and after Pink Morsel price increase on Jan 15, 2021", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

# Run server
if __name__ == '__main__':
    app.run(debug=True)
