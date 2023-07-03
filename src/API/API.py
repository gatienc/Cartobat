import json
import urllib.request
import os
import csv
import pandas as pd

from ..utils.time_formatting import local_to_utc, utc_to_local

class API:
    def __init__(self):
        """
        Initialize the API object.

        Args:
            API_KEY (str): The API key to use for authentication.
        """
        self.API_KEY = os.environ['API_KEY']  
        self.BaseURL = os.environ['SITE_URL']+'/'+self.API_KEY
    @staticmethod
    def __isValid(data):
        """
        Check if the API data is valid.

        Args:
            data (dict): The raw API data.

        Returns:
            bool: True if the data is valid, False otherwise.
        """
        return (data["erreur"] == 'no')
    @staticmethod
    def __make_request(url:str):
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
    @staticmethod
    def __toTimestampedDataFrame(data:list,toLocal:bool = True)->pd.DataFrame:
        """
        Transform the raw data from the API into a timestamped dataframe and pass to local time.
        Args:
            data (list): The raw data from the API.
            toLocal (bool, optional): If True, the timestamp is converted to local time. Defaults to True.
        Returns:
            pd.DataFrame: The timestamped dataframe.        
        """
        
        data=pd.DataFrame(data)
        data["timestamp"]=pd.to_datetime(data['timestamp'])
        
        if toLocal:
            data["timestamp"]=data["timestamp"].apply(utc_to_local)
        
        return data
    def getCartoWearList(self)->list:
        """
        Retrieves the CartoWear list from the API.

        Returns:
            list: The CartoWear list if valid, None otherwise.
        """
        # Sets up the URL to fetch the tag list.
        url = self.BaseURL + "/getCartoWearList"
        data = self.__make_request(url)
        # Extracts the list of tags from the response.
        if self.__isValid(data):
            CartoWearList = data["resultat"]
            return CartoWearList
        else:
            return None

    def getRawDataForCartoWear(self,MAC_WEAR:str,StartTimestamp:pd.Timestamp,EndTimestamp:pd.Timestamp,**kwargs)->list:
        """
        Retrieve the raw data for a given CartoWear tag and save it in a CSV file.

        Args:
            MAC_WEAR (str): The MAC_WEAR of the tag.
            StartTimestamp (pd.Timestamp): The start timestamp of the data.
            EndTimestamp (pd.Timestamp): The end timestamp of the data.
            **kwargs: Additional keyword arguments.
                filepath (str): if provided : will save data to the given path.

        Returns:
            list: The raw data if valid, None otherwise.
        """
        
        # format the timestamp to the UTC format
        StartTimestamp=local_to_utc(StartTimestamp)
        EndTimestamp=local_to_utc(EndTimestamp)
        
        # Sets up the URL to fetch the tag list.
        StartTimestamp=StartTimestamp.strftime("%Y-%m-%d%%20%H:%M:%S.%f")
        EndTimestamp=EndTimestamp.strftime("%Y-%m-%d%%20%H:%M:%S.%f")
        url = self.BaseURL + "/getRawDataForCartoWear/"+MAC_WEAR+"/"+StartTimestamp+"/"+EndTimestamp
        data=self.__make_request(url)
        # Extracts the list of tags from the response.
        if self.__isValid(data):
            result = data["resultat"]
            filepath=kwargs.get('filepath',False)
            if filepath:
            #save the result in a csv file
                with open(filepath, 'w', newline='') as csvfile:
                    fieldnames = ['timestamp', 'macModule', 'rssi']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    for row in result:
                        writer.writerow(row)
            return self.__toTimestampedDataFrame(result,toLocal=True)
    def getBuilding(self)->list:
        """
        Retrieve the list of buildings from the API.

        Returns:
            list: The list of buildings if valid, None otherwise.
        """
        # Sets up the URL to fetch the tag list.
        url = self.BaseURL + "/getBuilding"

        data=self.__make_request(url)
        # Extracts the list of tags from the response.
        if self.__isValid(data):
            result = data["resultat"]
            self.Building=result[0]
            return result
    def getLayersInBuilding(self,buildingid=None)->list:
        """
        Retrieve the list of layers in a building.

        Args:
            buildingid (int): The ID of the building. If not provided, the ID of the current building is used.

        Returns:
            list: The list of layers if valid, None otherwise.
        """
        # Sets up the URL to fetch the tag list.
        if buildingid==None:
            buildingid=self.Building['ID_batiment']
        url = self.BaseURL + "/getLayersInBuilding/"+str(buildingid)
        
        data=self.__make_request(url)
        # Extracts the list of tags from the response.
        if self.__isValid(data):
            result = data["resultat"]
            self.BuildingLayers=result
            return result    
    def getAreasInLayer(self,layerid=None)->list:
        """
        Retrieve the list of areas in a layer.

        Args:
            layerid (int): The ID of the layer. If not provided, the ID of the current layer is used.

        Returns:
            list: The list of areas if valid, None otherwise.
        """
        # Sets up the URL to fetch the tag list.
        if layerid==None:
            layerid=self.BuildingLayers['ID_batiment']
        url = self.BaseURL + "/getAreasInLayer/"+str(layerid)
        
        data=self.__make_request(url)
        # Extracts the list of tags from the response.
        if self.__isValid(data):
            result = data["resultat"]
            self.LayerAreas=result
            return result
    def getCartoModuleWithLocationList(self):
        """
        Retrieve the list of tags with their location.

        Returns:
            list: The list of tags with location if valid, None otherwise.
        """
        # Sets up the URL to fetch the tag list.
        url = self.BaseURL + "/getCartoModuleWithLocationList"
        
        data=self.__make_request(url)
        # Extracts the list of tags from the response.
        if self.__isValid(data):
            result = data["resultat"]
            self.CartoModuleWithLocationList=result
            return result

