import math
from typing import List, Tuple

class Vector2d:
    def __init__(self,x:int,y:int):
        self.x:int = x
        self.y:int = y
    
    def __sub__(self,vector:"Vector2d")->"Vector2d":
        if isinstance(vector,Vector2d):
            result_vector = self + vector.opposite_vector
            return result_vector
    def __add__(self,vector:"Vector2d")->"Vector2d":
        if(isinstance(vector,Vector2d)):

            new_x = self.x + vector.x
            new_y = self.y + vector.y
            result_vector = Vector2d(new_x,new_y)
        return result_vector
        
    def distance(self, vector:"Vector2d"):
        if(isinstance(vector,Vector2d)):
            lenght=self.distance_vector(vector).magnitude
            return lenght
    def distance_vector(self,vector:"Vector2d")->"Vector2d":
        if(isinstance(vector,Vector2d)):
            difference_vector = self - vector
            return difference_vector
    @property
    def opposite_vector(self) ->"Vector2d":
        new_x = -self.x
        new_y = -self.y
        result_vector = Vector2d(new_x,new_y)
        return result_vector
    @property
    def magnitude(self):
        lenght = math.sqrt(self.x **2 + self.y**2)
        return lenght
    def __eq__(self, vector:"Vector2d") -> bool:
        
        if(isinstance(vector,Vector2d)):
            return self.x == vector.x and self.y==vector.y
    def __hash__(self):
        return hash((self.x,self.y))
        
    def __repr__(self):
        return str((self.x,self.y))
    def translate(self,x:int=0,y:int=0):
        
        if(x!=0):
            self.x = x
        if(y!=0):
            self.y=y 




