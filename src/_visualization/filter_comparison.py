import plotly.graph_objects as go
def add_line_plot(df,fig, filter_col, filter_val, x_col, y_col, title):
    """
    Add a line Plot to the fig 
    Args:
        df (pd.DataFrame): The dataframe to plot
        fig (go.Figure): The figure to add the plot to
        filter_col (str): The column to filter on
        filter_val (str): The value to filter on
        x_col (str): The column to use as x axis
        y_col (str): The column to use as y axis
        title (str): The title of the plot
    Output:
        go.Figure: The figure with the plot added
    
    
    """
    df = df[df[filter_col] == filter_val]
    x_col = df[x_col]
    y_col = df[y_col]
    fig.add_trace(go.Scatter(x=x_col, y=y_col,
                    mode='lines+markers',
                    name=title))
    return fig
