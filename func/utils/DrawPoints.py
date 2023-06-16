import folium
def DrawPoints(map_object, list_of_points, layer_name, line_color, fill_color, text):
    """
    Function to draw points in the map
    
    input:
    map_object: folium map object
    list_of_points: list of points to draw
    layer_name: name of the layer
    line_color: color of the line
    fill_color: color of the fill
    text: text to display in the popup
    
    output:    
    """

    fg = folium.FeatureGroup(name=layer_name)

    for point in list_of_points:
        fg.add_child(
            folium.CircleMarker(
                point,
                radius=1,
                color=line_color,
                fill_color=fill_color,
                popup=(folium.Popup(text)),
            )
        )

    map_object.add_child(fg)