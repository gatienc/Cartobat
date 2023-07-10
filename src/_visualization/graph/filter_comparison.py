import plotly.graph_objects as go
from src._preprocessing.Preprocessor import Preprocessor
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

def filtering_comparator(preprocessor:Preprocessor,filter_list:list,mac_module_id:str,show:bool=False,name_list=None):
        '''
        This function is used to compare the effect of different filters on the same data
        cleaner must have been set before calling this function
        
        Args:
            preprocessor (Preprocessor): The preprocessor to use (cleaner must have been set)
            filter_list (list): The list of filters to compare
            mac_module_id (str): The mac module id to plot
            show (bool, optional): If true show the plot. Defaults to False.
            name_list (list, optional): The list of names to use for the filters. Defaults to None.
        '''
        #tricks to get the name of the filters
        if name_list is None:
                name_list=[]
                for filter in filter_list:
                        name_list.append(filter.__class__.__name__)
        #plotting
        fig=go.Figure()
        fig=add_line_plot(preprocessor.rssi_df,fig, 'macModule', mac_module_id, 'timestamp', 'rssi', 'raw_data')
        for index,filter in enumerate(filter_list):
                data=preprocessor.set_filter(filter).process()
                fig=add_line_plot(data,fig, 'macModule', mac_module_id, 'timestamp', 'rssi', name_list[index])
        if show: fig.show()
        return fig
