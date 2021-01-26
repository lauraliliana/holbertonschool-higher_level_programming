#!/usr/bin/python3
""" Module of a class base """
import json


class Base:
    """ A base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor """
        if id == None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns a json representation of a list of dict """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of a list to a file """
        filename = cls.__name__ + ".json"
        lsto = []
        if lsto is not None:
            for i in list_objs:
                lsto.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(lsto))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @staticmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = cls.__name__ + ".json"
        ls = []
        try:
            with open(filename, 'w') as f:
                ls = cls.to_json_string(f.read())
            for i in enumerate(ls):
                ls[i] = cls.create(**ls[i])
        except:
            pass
        return ls
