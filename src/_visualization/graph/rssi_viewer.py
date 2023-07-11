import plotly.graph_objects as go
from .add_line_plot import add_line_plot

def rssi_viewer(rssi_df):
    '''
        This function is used to visualize the rssi data of every mac_module in the rssi_df
        
        Args:
            rssi_df (pandas.dataframe ): The rssi_df to visualize
        
    '''
    fig=go.Figure()
    for mac_module_id in rssi_df['macModule'].unique():
        fig=add_line_plot(rssi_df,fig, 'macModule', mac_module_id, 'timestamp', 'rssi', mac_module_id)
    fig.show()
    return fig
