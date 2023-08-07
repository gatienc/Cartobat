from shapely.geometry import Polygon
import math

def discrete_circle(n:int,center:tuple,radius:float)->Polygon:
    """
    Create a shapely.polygon with n points on the circle
    """
    print(f"center={center} radius={radius}")

    points=[]
    for i in range(n):
        x=center[0]+radius*math.cos(2*math.pi*i/n)
        y=center[1]+radius*math.sin(2*math.pi*i/n)
        points.append((x,y))
    return Polygon(points)


if __name__=='__main__':
    import plotly.graph_objs as go

    def polygon_trace(polygon:Polygon,title:str="Polygon"):

        # extract the x and y coordinates of the polygon exterior
        x, y = polygon.exterior.xy
        # convert the numpy.ndarray to a list
        x = x.tolist()
        y = y.tolist()
        return (go.Scatter(x=x, y=y, mode='lines',name=title))

    # create a Plotly scatter plot with mode='lines'
    fig = go.Figure()

    for k in range(4,20):
        octogon=discrete_circle(k,(0,0), 1)
        fig.add_trace(polygon_trace(octogon,title=str(k)))

    # set the plot layout
    fig.update_layout(
        xaxis_title='X',
        yaxis_title='Y',
        width=500,
        height=500,
    )

    # show the plot
    fig.show()
