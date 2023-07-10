import csv
def save_cartomodule(callAPI,MapName):
    """
    give the name of the map and the API object
    will create a csv file in data folder containing the marker
    
    args:
        callAPI: API object
        MapName: str
    
    """

    modules=callAPI.getCartoModuleWithLocationList()
    with open('data/carteModule'+MapName+'.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(modules[0].keys())
        for item in modules:
            print(item)
            writer.writerow(item.values())
    csv_file.close()
