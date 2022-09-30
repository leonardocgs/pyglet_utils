import pyglet
from Rectangle import Rectangle
from Vector2d import Vector2d


class GameObject():

    def __init__(self,position:"Vector2d",img_path:str,batch=None, rotation = 0):
        self._image = pyglet.resource.image(img_path)
        self._image.anchor_x = self._image.width //2
        self._image.anchor_y = self._image.height // 2 
        self._width = self._image.width
        self._height = self._image.height
        self._rotation = rotation
        self._position = position 
        self._rectangle = Rectangle(position,self._width,self._height,self._rotation)
        self._sprite = pyglet.sprite.Sprite(self._image,x = self._rectangle.x, y = self._rectangle.y,batch=batch)
        
    def connect_GameObject_with_rectangle(self):
        self._sprite.x = self._rectangle.x
        self._sprite.y =self._rectangle.y
    @property
    def center(self):
         return self._rectangle.center
    def draw(self):
        self._sprite.draw()
    def delete(self):
        self._sprite.delete()
    @property
    def mid_left(self):
         return self._rectangle.mid_left
    @property
    def mid_right(self):
        return self._rectangle.mid_right
    @property
    def mid_top(self):
        return self._rectangle.mid_top
    @property
    def mid_bottom(self):
        return self._rectangle.mid_bottom
    @property
    def top_left(self):
        return self._rectangle.top_left
    @property
    def top_right(self):
        return self._rectangle.top_right
    @property
    def bottom_left(self):
        return self._rectangle.bottom_left
    @property
    def bottom_right(self):
        return self._rectangle.bottom_right    
    @property
    def rotation(self):
        return self._rectangle.rotation
    @property
    def left(self):
        return self._rectangle.left
    @property
    def right(self):
        return self._rectangle.right
    @property
    def top(self):
         return self._rectangle.top
    @property
    def bottom(self):
         return self._rectangle.bottom
    @property
    def position(self):
         return (self._position.x, self._position.y)
    @property
    def scale(self):
        return self._sprite.scale
    @property
    def x(self):
        return self._sprite.x
    @property
    def width(self):
        return self._rectangle.width
    @property
    def height(self):
        return self._rectangle.height
    @property
    def y(self):
        return self._sprite.x
    @position.setter
    def position(self,vector_position:"Vector2d"):
        self._rectangle.position = vector_position    
        self.connect_GameObject_with_rectangle()
    @center.setter
    def center(self,new_center:"Vector2d"):
        self._rectangle.center = new_center
        self.connect_GameObject_with_rectangle()
    @mid_left.setter
    def mid_left(self,new_mid_left:"Vector2d"):
        self._rectangle.mid_left = new_mid_left
        self.connect_GameObject_with_rectangle()
    @mid_right.setter
    def mid_right(self,new_mid_right:"Vector2d"):
        self._rectangle.mid_right = new_mid_right
        self.connect_GameObject_with_rectangle()
    @mid_top.setter
    def mid_top(self,new_mid_top:"Vector2d"):
        self._rectangle.mid_top = new_mid_top
        self.connect_GameObject_with_rectangle()
    @mid_bottom.setter
    def mid_bottom(self,new_mid_bottom:"Vector2d"):
        self._rectangle.mid_bottom = new_mid_bottom
        self.connect_GameObject_with_rectangle()
    @top_left.setter
    def top_left(self,top_left:"Vector2d"):
        self._rectangle.top_left = top_left
    @scale.setter
    def scale(self,size):

        self._sprite.scale = size
        self._rectangle.height = self._sprite.height
        self._rectangle.width = self._sprite.width
        self.connect_GameObject_with_rectangle()
    @position.setter
    def position(self,vector_position:"Vector2d"):
        self._rectangle.position = vector_position    
        self.connect_GameObject_with_rectangle()
    @center.setter
    def center(self,new_center:"Vector2d"):
        self._rectangle.center = new_center
        self.connect_GameObject_with_rectangle()
    @mid_left.setter
    def mid_left(self,new_mid_left:"Vector2d"):
        self._rectangle.mid_left = new_mid_left
        self.connect_GameObject_with_rectangle()
    @mid_right.setter
    def mid_right(self,new_mid_right:"Vector2d"):
        self._rectangle.mid_right = new_mid_right
        self.connect_GameObject_with_rectangle()
    @mid_top.setter
    def mid_top(self,new_mid_top:"Vector2d"):
        self._rectangle.mid_top = new_mid_top
        self.connect_GameObject_with_rectangle()
    @mid_bottom.setter
    def mid_bottom(self,new_mid_bottom:"Vector2d"):
        self._rectangle.mid_bottom = new_mid_bottom
        self.connect_GameObject_with_rectangle()
    @top_left.setter
    def top_left(self,top_left:"Vector2d"):
        self._rectangle.top_left = top_left
        self.connect_GameObject_with_rectangle()
    @top_right.setter
    def top_right(self,top_right:"Vector2d"):
        self._rectangle.top_right = top_right
        self.connect_GameObject_with_rectangle()
    @bottom_left.setter
    def bottom_left(self,bottom_left:"Vector2d"):
        self._rectangle.bottom_left = bottom_left
        self.connect_GameObject_with_rectangle()
    @bottom_right.setter
    def bottom_right(self,bottom_right:"Vector2d"):
        self._rectangle.bottom_right = bottom_right
        self.connect_GameObject_with_rectangle()
    @x.setter
    def x(self,new_x:int):
        self._rectangle.x = new_x
        self.connect_GameObject_with_rectangle()
    @y.setter
    def y(self,new_y:int):
        self._rectangle.y = new_y
        self.connect_GameObject_with_rectangle()
    @left.setter
    def left(self,distance:int):
        self._rectangle.left = distance
        self.connect_GameObject_with_rectangle()
         
    @right.setter
    def right(self,distance:int):
    
        self._rectangle.right = distance
        self.connect_GameObject_with_rectangle()
    @top.setter
    def top(self,distance:int):
        self._rectangle.top = distance
        self.connect_GameObject_with_rectangle()
    
    @bottom.setter
    def bottom(self,distance:int):
        self._rectangle.bottom = distance
        self.connect_GameObject_with_rectangle()
    @rotation.setter
    def rotation(self, angle:int):
        self._rectangle.rotation = angle
        self.connect_GameObject_with_rectangle()
        self._sprite.rotation = angle
