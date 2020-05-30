from core.record import RecordOnScreen
from core.visitor import Visitor
import json
import logging

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance


class Root(Singleton, RecordOnScreen):
    """ Class representing mind Root.
    As there can be only one Root, Singleton pattern is used.
    """
    def __init__(self, y: int, x: int):
        super(Root, self).__init__(y, x)

    def serialize(self, f_name: str='mindpy.json'):
        with open(f_name, 'w') as f:
            f.write(json.dumps(self.toJSON()))

    @staticmethod
    def deserialize(f_name):
        with open(f_name, 'r') as f:
            f_tree = f.read()

        def create_record(r_dict):
            rec = RecordOnScreen(r_dict['y'], r_dict['x'])
            rec.data = r_dict['data']
            rec.children = [create_record(child) for child in r_dict['children']]
            return rec

        tree = json.loads(f_tree)
        root = Root(tree['y'], tree['x'])
        root.data = tree['data']
        root.children = [create_record(child) for child in tree['children']]

        return root

