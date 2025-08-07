# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',
                                                options=[
                                                    {'label': 'All Sites', 'value': 'ALL'},
                                                    {'label': 'site1', 'value': 'site1'},
                                                    {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                                    {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                                                    {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                                    {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                                                                                        
                                                ],
                                                value="ALL",
                                                placeholder="Select a Launch Site here",
                                                searchable=True
                                                
                                            ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(
                                    id='payload-slider',
                                    min = 0,
                                    max = 10000,
                                    step = 1000,
                                    marks={0: '0', 100: '100'},
                                    value = [min_payload, max_payload]
                                ),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id="success-pie-chart", component_property='figure'),
              Input(component_id='site-dropdown', component_property='value')
            )
def get_pie_chart(selected_site):
    # ALL sites: show total successful launches by site
    if selected_site == "ALL":
        # filter only successes
        df_success = spacex_df[spacex_df["class"] == 1]
        fig = px.pie(
            df_success,
            names="Launch Site",
            title="Total Successful Launches by Site"
        )
    # Single site: show success vs. failure for that site
    else:
        df_site = spacex_df[spacex_df["Launch Site"] == selected_site]
        # value_counts yields a Series {1: count_success, 0: count_failure}
        counts = df_site["class"].value_counts().rename({1: "Success", 0: "Failure"})
        fig = px.pie(
            names=counts.index,
            values=counts.values,
            title=f"Launch Outcomes for {selected_site}"
        )
    return fig
        

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [
                Input(component_id='site-dropdown', component_property='value'),
                Input(component_id='payload-slider', component_property='value')
              ]
              )
def get_scatter_chart(selected_site, payload_range):
    low, high = payload_range
    # filter by payload mass
    mask = (
        (spacex_df["Payload Mass (kg)"] >= low) &
        (spacex_df["Payload Mass (kg)"] <= high)
    )
    filtered_df = spacex_df[mask]

    # further filter by site if not ALL
    if selected_site != "ALL":
        filtered_df = filtered_df[
            filtered_df["Launch Site"] == selected_site
        ]

    # scatter: payload vs class, colored by booster version
    fig = px.scatter(
        filtered_df,
        x="Payload Mass (kg)",
        y="class",
        color="Booster Version Category",
        title="Payload vs. Launch Outcome"
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run()
