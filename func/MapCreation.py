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