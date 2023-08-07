from src.DataLoader import Receiver
from src.utils.geometry import discrete_circle,intersection
import rtree
class ZoneSelector():
    def __init__(self,room_r_tree:rtree,room_dict:dict):
      self.Threshold1 = -40
      self.Threshold2 = -75
      self.radius1=2.5
      self.radius2=5
      self.room_r_tree=room_r_tree
      self.room_dict=room_dict
    def set_threshold(self,Threshold1:int,Threshold2:int):
        self.Threshold1=Threshold1
        self.Threshold2=Threshold2
    def set_radius(self,radius1:float,radius2:float):
        self.radius1=radius1
        self.radius2=radius2
    def zone_selection(self,receiver:Receiver,rssi:int):
      """
      Return the predicted zone for the selected receiver receiving the rssi 
      
      Parameters
      ---
      Input:
      receiver: Receiver
      rssi: int
      
      Output:
      List of Polygon
      """
      if rssi>=self.Threshold1:
        #return the room in wich the receiver is
        return [receiver.room.cartesian_polygon]
      
      elif self.Threshold2< rssi < self.Threshold1:
          #return all the room in wich the receiver is
          point=receiver.cartesian_point
          area=discrete_circle(6,[point.x,point.y],2.5)#create an hexagon with 6 points centered on the receiver
          rooms=list(intersection(area,self.room_r_tree,self.room_dict))
          return rooms
      elif rssi<=self.Threshold2:
          point=receiver.cartesian_point
          area=discrete_circle(6,[point.x,point.y],5)#create an hexagon with 6 points centered on the receiver
          rooms=list(intersection(area,self.room_r_tree,self.room_dict))
          return rooms