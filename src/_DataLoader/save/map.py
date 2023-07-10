import csv
def save_map(callAPI,MapName):
    """
    give the name of the map and the API object
    will create a csv file in data folder containing the map
    
    """
    Layers=callAPI.getLayersInBuilding()
    if len(Layers)==0:
        ID_couche=Layers[0]["ID_couche"]
    else:
        print("this layers are able",Layers)
        choose=int(input("choose a layer"))
        ID_couche=Layers[choose]["ID_couche"]
        
    data=callAPI.getAreasInLayer(ID_couche)
    with open('data/'+MapName+'.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(data[0].keys())
        for item in data:
            print(item)
            writer.writerow([item['ID_element'],eval(item["coordinates"])[0],item['nom']])
    csv_file.close()