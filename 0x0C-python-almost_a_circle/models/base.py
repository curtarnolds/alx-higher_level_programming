#!/usr/bin/python3
"""Base module for all classes in the models package."""
import json
import csv


class Base:
    """A base class."""
    __nb_objects = 0

    def __init__(self, id: int = None) -> None:
        """Initialize a Base instance.

        Args:
            id: An optional id value.
        """
        if id:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects

    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (dict): A Python dictionary.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of list_objs to file.

        Args:
            list_objs (list): List of instances that inherit from Base.
        """
        with open(f"{cls.__name__}.json", mode='w') as json_file:
            list_dict = [item.to_dictionary() for item in list_objs]
            json_dict = cls.to_json_string(list_dict)
            json_file.write(json_dict)

    def from_json_string(json_string):
        """Return the list of the JSON string representation
        of json_string.

        Args:
            json_string (str): A JSON string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set.

        Args:
            dictionary (str): string representation of a dictionary.
        """
        dummy_dict = cls(2, 3)
        for key, value in dictionary.items():
            setattr(dummy_dict, key, value)
        return dummy_dict

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        try:
            with open(f"{cls.__name__}.json") as json_file:
                dict_list = cls.from_json_string(json_file.read())
                return [cls.create(**item) for item in dict_list]
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize from csv."""
        try:
            with open(f"{cls.__name__}.csv", 'rt') as csv_file:
                reader = csv.reader(csv_file)
                keys = reader.__next__()
                dict_list = []
                for value in reader:
                    dict_list.append({k: int(v) for k, v in zip(keys, value)})
                return [cls.create(**item) for item in dict_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize to CSV."""
        with open(f"{cls.__name__}.csv", 'wt') as csv_file:
            list_dict = [item.to_dictionary() for item in list_objs]
            keys = list_dict[0].keys()
            writer = csv.writer(csv_file)
            writer.writerow(keys)
            for item in list_dict:
                writer.writerow(item.values())
