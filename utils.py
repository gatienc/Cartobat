
from secret import API_KEY,MAC_WEAR
import csv
from API import API
import pandas as pd
##get the map of palaiseau in csv
def get_Map_csv():
    Gatien_API=API(API_KEY) 
    building=Gatien_API.getBuilding()
    Layers=Gatien_API.getLayersInBuilding()
    ID_couche=Layers[0]["ID_couche"]
    data=Gatien_API.getAreasInLayer(ID_couche)
    with open('data/cartePalaiseau.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(data[0].keys())
        for item in data:
            print(item)
            writer.writerow([item['ID_element'],eval(item["coordinates"])[0],item['nom']])
    csv_file.close()

Gatien_API=API(API_KEY)
hour_correction=2
start=pd.to_datetime("2023-06-01 14:35:46.000000")-pd.Timedelta(hour_correction, unit="h")
end=pd.to_datetime("2023-06-01 14:53:00.000000")-pd.Timedelta(hour_correction, unit="h")

Gatien_API.getRawDataForCartoWear(MAC_WEAR,start,end,"data/manip1.1.csv")

# modules=Gatien_API.getCartoModuleWithLocationList()
# with open('data/carteModulePalaiseau.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(modules[0].keys())
#     for item in modules:
#         print(item)
#         writer.writerow(item.values())
# csv_file.close()
