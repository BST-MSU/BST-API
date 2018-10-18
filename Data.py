from enum import Enum

class BST_FIELD(Enum):
    """"
    values castable to doubles will be assigned values less than 100
    values castable only as strings will be assigned values greater than 200
    """"

class DataPacket:
    def __init__():
        self.data = {}
    
    def get_field(self, field):
        return data[field]
    
    def set_field(self, field, value):
        if typeof(field) is BST_FIELD:
            data[field] = value
            return 1
        return 0
        
    def serialize():
        pass

    def deserialize():
        pass   
