import pandas
import plotly.express as px


def create_map(values):
    colNames = ["state", "value"]
    dictOfStates = {
        "AL": ["AL", values[0]],
        "AK": ["AK", values[1]],
        "AZ": ["AZ", values[2]],
        "AR": ["AR", values[3]],
        "CA": ["CA", values[4]],
        "CO": ["CO", values[5]],
        "CT": ["CT", values[6]],
        "DE": ["DE", values[7]],
        "DC": ["DC", values[8]],
        "FL": ["FL", values[9]],
        "GA": ["GA", values[10]],
        "HI": ["HI", values[11]],
        "ID": ["ID", values[12]],
        "IL": ["IL", values[13]],
        "IN": ["IN", values[14]],
        "IA": ["IA", values[15]],
        "KS": ["KS", values[16]],
        "KY": ["KY", values[17]],
        "LA": ["LA", values[18]],
        "ME": ["ME", values[19]],
        "MD": ["MD", values[20]],
        "MA": ["MA", values[21]],
        "MI": ["MI", values[22]],
        "MN": ["MN", values[23]],
        "MS": ["MS", values[24]],
        "MO": ["MO", values[25]],
        "MT": ["MT", values[26]],
        "NE": ["NE", values[27]],
        "NV": ["NV", values[28]],
        "NH": ["NH", values[29]],
        "NJ": ["NJ", values[30]],
        "NM": ["NM", values[31]],
        "NY": ["NY", values[32]],
        "NC": ["NC", values[33]],
        "ND": ["ND", values[34]],
        "OH": ["OH", values[35]],
        "OK": ["OK", values[36]],
        "OR": ["OR", values[37]],
        "PA": ["PA", values[38]],
        "RI": ["RI", values[39]],
        "SC": ["SC", values[40]],
        "SD": ["SD", values[41]],
        "TN": ["TN", values[42]],
        "TX": ["TX", values[43]],
        "UT": ["UT", values[44]],
        "VT": ["VT", values[45]],
        "VA": ["VA", values[46]],
        "WA": ["WA", values[47]],
        "WV": ["WV", values[48]],
        "WI": ["WI", values[49]],
        "WY": ["WY", values[50]]}

    state_df = pandas.DataFrame.from_dict(dictOfStates, orient='index')

    state_df.columns = colNames

    fig = px.choropleth(state_df,  # Input Pandas DataFrame
                        locations="state",  # DataFrame column with locations
                        color="value",  # DataFrame column with color values
                        hover_name="state",  # DataFrame column hover info
                        locationmode='USA-states')  # Set to plot as US States
    fig.update_layout(
        title_text='Federal Student Loan Portfolio by Borrower Location (per Billion Dollars)',  # Create a Title
        geo_scope='usa',  # Plot only the USA instead of globe
    )
    fig.show()  # Output the plot to the screen
    fig.write_html(f'../../docs/output/map.html')


class InteractiveMapUnitedStates:

    def __init__(self, balance):
        create_map(balance)
