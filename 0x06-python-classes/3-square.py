#!/usr/bin/python3
<<<<<<< HEAD
""" A
=======
""" Module """
class Square:
    """ Defines the Square class"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
>>>>>>> d882e90c21e820660dff0734f2c62c8cf70da5ad
