class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height
    
    def set_width(self, width):
        self.width=width
    
    def set_height(self, height):
        self.height=height
    
    def get_area(self):
        return (self.width*self.height)
    
    def get_perimeter(self):
        return (2*self.height + 2*self.width)
    
    def get_diagonal(self):
        return ((self.width ** 2 +self.height **2)** .5)
    
    def get_picture(self):
        if((self.width<=50)and(self.height<=50)):
            res=""
            for i in range(self.height):
                res+="*"*self.width+"\n"
            return res    
        return("Too big for picture.")
    
    def get_amount_inside(self, another):
        horizontal=self.width//another.width
        vertical=self.height//another.height
        return vertical*horizontal
    
    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)
    
class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)
    
    def set_height(self, side):
        self.height=side
        self.width=side
    
    def set_width(self, side):
        self.height=side
        self.width=side

    def set_side(self, side):
        self.height=side
        self.width=side
        
    
    def __str__(self):
        return "Square(side={})".format(self.width)
    



