import geopandas as gpd
import folium

def MeanMarkerPosition(marker_gdf):
    long=[x for x in marker_gdf["geometry"].x]
    lat=[y for y in marker_gdf["geometry"].y]
    #get the average of long list
    long= sum(long) / len(long)
    lat= sum(lat) / len(lat)
    location=[lat,long]
    return location

def MapCreation(map_gdf,**kwargs):
    if "marker_gdf" in kwargs:
        marker_gdf=kwargs["marker_gdf"]
    if "marker_gdf" in kwargs and "location" not in kwargs:
        location=MeanMarkerPosition(marker_gdf)
    elif "location" in kwargs:
        location=kwargs["location"]
    else:
        raise TypeError("No location given")
    m = folium.Map(location = location,max_zoom=30, zoom_start=20,crs="EPSG3857")
    tooltip = folium.features.GeoJsonTooltip(fields=['ID_element', 'nom'], 
                                            labels=True,
                                            stick=False,
                                            )
    if "marker_gdf" in kwargs:
        tooltip_marker = folium.features.GeoJsonTooltip(fields=['macModule'], 
                                                labels=True,
                                                stick=False)
    folium.GeoJson(map_gdf, tooltip=tooltip).add_to(m)
    if "marker_gdf" in kwargs:
        folium.GeoJson(marker_gdf, tooltip=tooltip_marker).add_to(m)
    return m

