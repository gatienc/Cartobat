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
def MapCreation(map_gdf,marker_gdf):
    location=MeanMarkerPosition(marker_gdf)
    m = folium.Map(location = location,max_zoom=30, zoom_start=20,crs="EPSG3857")
    tooltip = folium.features.GeoJsonTooltip(fields=['ID_element', 'nom'], 
                                            labels=True,
                                            stick=False,
                                            )
    tooltip_marker = folium.features.GeoJsonTooltip(fields=['macModule'], 
                                            labels=True,
                                            stick=False)
    folium.GeoJson(map_gdf, tooltip=tooltip).add_to(m)
    folium.GeoJson(marker_gdf, tooltip=tooltip_marker).add_to(m)
    return m

def FoliumZoneLayer(map_gdf:gpd.GeoDataFrame,color='blue'):
    ZoneLayer=folium.GeoJson(map_gdf, 
                    tooltip = folium.features.GeoJsonTooltip(fields=['ID_element', 'nom'], 
                                            labels=True,
                                            stick=False,
                                            ),
                    style_function=lambda x: {
                                'fillColor': color,
                                'fillOpacity': 0.5,
                                'weight': 0.1
                            })
    return ZoneLayer