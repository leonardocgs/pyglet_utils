from Vector2d import Vector2d
import copy
class Rectangle:

    def __init__(self,middle_point:"Vector2d" ,_width:float,_height:float, rotation = 0):

        self.width = _width
        self.height = _height
        self._center = middle_point
        self.rotation = rotation
    @property
    def center(self):
        return copy.copy(self._center)
    @property
    def mid_left(self):
        return copy.copy(self._midleft)
    @property
    def mid_right(self):
        return copy.copy(self._midright)
    @property
    def mid_top(self):
        return copy.copy(self._midtop)
    @property
    def mid_bottom(self):
        return copy.copy(self._midbottom)
    @property
    def top_left(self):
        return copy.copy(self._topleft)
    @property
    def top_right(self):
        return copy.copy(self._topright)
    @property
    def bottom_left(self):
        return copy.copy(self._bottomleft)
    @property
    def bottom_right(self):
        return copy.copy(self._bottomright)
    @property
    def rotation(self):
        return self._rotation
    @property
    def x(self):
        return self.center.x
    @property
    def y(self):
        return self.center.y
    @center.setter
    def center(self,new_center:"Vector2d"):
        if (isinstance(new_center,Vector2d)):
            self._center = new_center 
            self.__compute_points()
    @mid_left.setter
    def mid_left(self,new_mid_left:"Vector2d"):
        if (isinstance(new_mid_left,Vector2d)):
            vector_to_add = new_mid_left.distance_vector(self._midleft) 
            self.center += vector_to_add
            self.__compute_points()
    @mid_right.setter
    def mid_right(self,new_mid_right:"Vector2d"):
        if (isinstance(new_mid_right,Vector2d)):
            vector_to_add = new_mid_right.distance_vector(self._midright) 
            self.center += vector_to_add
            self.__compute_points()
    @mid_top.setter
    def mid_top(self,new_mid_top:"Vector2d"):
        if (isinstance(new_mid_top,Vector2d)):
            vector_to_add = new_mid_top.distance_vector(self._midtop) 
            self.center += vector_to_add
            self.__compute_points()
    @mid_bottom.setter
    def mid_bottom(self,new_mid_bottom:"Vector2d"):
        if (isinstance(new_mid_bottom,Vector2d)):
            vector_to_add = new_mid_bottom.distance_vector(self._midbottom) 
            self.center += vector_to_add
            self.__compute_points()
    @top_left.setter
    def top_left(self,top_left:"Vector2d"):
        if (isinstance(top_left,Vector2d)):
            vector_to_add = top_left.distance_vector(self._topleft) 
            self.center += vector_to_add
            self.__compute_points()
    @top_right.setter
    def top_right(self,top_right:"Vector2d"):
        if (isinstance(top_right,Vector2d)):
            vector_to_add = top_right.distance_vector(self._topright) 
            self.center += vector_to_add
            self.__compute_points()
    @bottom_left.setter
    def bottom_left(self,bottom_left:"Vector2d"):
        if (isinstance(bottom_left,Vector2d)):
            vector_to_add = bottom_left.distance_vector(self._bottomleft) 
            self.center += vector_to_add
            self.__compute_points()
    @bottom_right.setter
    def bottom_right(self,bottom_right:"Vector2d"):
        if (isinstance(bottom_right,Vector2d)):
            vector_to_add = bottom_right.distance_vector(self._bottomright) 
            self.center += vector_to_add
            self.__compute_points()
    @x.setter
    def x(self,new_x:int):
        self.center = Vector2d(new_x,self.y)
        self.__compute_points()
    @y.setter
    def y(self,new_y:int):
        self.center = Vector2d(self.x,new_y)
        self.__compute_points()
    @rotation.setter
    def rotation(self, angle:int):
        if(angle == 90 or angle == 270):
            self._height = self.width
            self._width = self.height
        elif (angle == 0 or angle ==180):
            self._height = self.height
            self._width = self.width
        self.__compute_points()
        self._rotation = angle
    def __compute_points(self):
        half__width = self._width /2 
        half__height = self._height /2
        self._midleft = Vector2d(self.center.x - half__width,self.center.y)
        self._midright = Vector2d(self.center.x + half__width,self.center.y)
        self._midtop = Vector2d(self.center.x, self.center.y + half__height)
        self._midbottom = Vector2d(self.center.x, self.center.y - half__height)
        self.__compute_auxiliar_points()

    def __compute_auxiliar_points(self):
        half__width = self._width /2 
        half__height = self._height /2
        self._topright = Vector2d(self._midtop.x+half__width,self._midtop.y)
        self._topleft = Vector2d(self._midtop.x-half__width,self._midtop.y)
        self._bottomright = Vector2d(self._midbottom.x+half__width,self._midbottom.y)
        self._bottomleft = Vector2d(self._midbottom.x-half__width,self._midbottom.y)
