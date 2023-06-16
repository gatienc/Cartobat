import json
import urllib.request
from secret import API_KEY
import csv
import pandas as pd


class API:
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY
        self.BaseURL = "https://cartobat.net/"+API_KEY
    def isValid(self,data):
        "check if the data is valid by taking the raw API data as input"
        return (data["erreur"] == 'no')  
    def getCartoWearList(self):
        print("getCartoWearList")
        # Sets up the URL to fetch the tag list.
        url = self.BaseURL + "/getCartoWearList"
        data = self.make_request(url)
        # Extracts the list of tags from the response.
        if self.isValid(data):
            CartoWearList = data["resultat"]
            return CartoWearList
        else:
            return None
        #to print the list of tags
        # if self.isValid(data):
        #     # Prints the list of tags.
        #     for CartoWear in CartoWearList:
        #         print(CartoWear['macwear'])
    def make_request(self, url:str):
        """
        Make an API request to the specified URL and return the obtained data.

        Args:
            url (str): The URL of the API to request.

        Returns:
            dict: The data returned by the API, as a dictionary.

        Raises:
            urllib.error.URLError: If an error occurs during the request.
            json.JSONDecodeError: If an error occurs while decoding the JSON data.
        """
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        data = json.loads(response.read())
        return data
    def getRawDataForCartoWear(self,MAC_WEAR:str,StartTimestamp:pd.Timestamp,EndTimestamp:pd.Timestamp,filepath:str):
        '''
        get the raw data for a given tag and save it in a csv file
        MAC_WEAR: the MAC_WEAR of the tag
        TimeStamp.format: '2023-06-01%2008:45:00.000'
        StartTimestamp: the start timestamp of the data
        EndTimestamp: the end timestamp of the data
        '''
        StartTimestamp=StartTimestamp.strftime("%Y-%m-%d%%20%H:%M:%S.%f")
        EndTimestamp=EndTimestamp.strftime("%Y-%m-%d%%20%H:%M:%S.%f")
        # Sets up the URL to fetch the tag list.
        url = self.BaseURL + "/getRawDataForCartoWear/"+MAC_WEAR+"/"+StartTimestamp+"/"+EndTimestamp

        data=self.make_request(url)
        # Extracts the list of tags from the response.
        if self.isValid(data):
            result = data["resultat"]
            #save the result in a csv file
            with open(filepath, 'w', newline='') as csvfile:
                fieldnames = ['timestamp', 'macModule', 'rssi']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in result:
                    writer.writerow(row)
    def getBuilding(self):
        '''
        get the list of building
        '''
        # Sets up the URL to fetch the tag list.
        url = self.BaseURL + "/getBuilding"

        data=self.make_request(url)
        # Extracts the list of tags from the response.
        if self.isValid(data):
            result = data["resultat"]
            self.Building=result[0]
            return result
    def getLayersInBuilding(self,buildingid=None):
        '''
        get the list of layers in a building
        '''
        # Sets up the URL to fetch the tag list.
        if buildingid==None:
            buildingid=self.Building['ID_batiment']
        url = self.BaseURL + "/getLayersInBuilding/"+str(buildingid)
        
        data=self.make_request(url)
        # Extracts the list of tags from the response.
        if self.isValid(data):
            result = data["resultat"]
            self.BuildingLayers=result
            return result    
    def getAreasInLayer(self,layerid=None):
        '''
        get the list of areas in a layer
        '''
        # Sets up the URL to fetch the tag list.
        if layerid==None:
            layerid=self.BuildingLayers['ID_batiment']
        url = self.BaseURL + "/getAreasInLayer/"+str(layerid)
        
        data=self.make_request(url)
        # Extracts the list of tags from the response.
        if self.isValid(data):
            result = data["resultat"]
            self.LayerAreas=result
            return result
    def getCartoModuleWithLocationList(self):
        '''
        get the list of tags with their location
        '''
        # Sets up the URL to fetch the tag list.
        url = self.BaseURL + "/getCartoModuleWithLocationList"
        
        data=self.make_request(url)
        # Extracts the list of tags from the response.
        if self.isValid(data):
            result = data["resultat"]
            self.CartoModuleWithLocationList=result
            return result

   
