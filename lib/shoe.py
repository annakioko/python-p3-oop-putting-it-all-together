#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def size(self):
        return self._size
    
    def set_size(self, size):
        if isinstance(size,int):
            self._size = size
        else:
            print("size must be an integer")
    
    size = property(size,set_size)
    

    def condition(self):
        return self.condition
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
    

            