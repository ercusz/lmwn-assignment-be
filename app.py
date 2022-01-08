# Python 3.8
# Author: Wachirawitch Y. <wachirawitch@kkumail.com>
#
########################## Problem ##############################
#   - find dict with key="email" then set value = "redacted"    #
#   - find dict with key="password" then remove it!             #
#   - allowed type = list, str, bytes, dict, tuple, int, float  #
#################################################################

value = {
    "email": "test@example.com",
    "password": "test",
    "user_info": {
        "name": "Test user",
        "email": "test@example.com",
    },
}
value_list = [
        "Hello", 
        1234, 
        6.6789, 
        [
            'A',
            'B',
            { 
                "email": "test@example.com", 
                'password': 'hello',
                'hiw_kaaw': 'somtum'
            },
        ], 
        10.123, 
        { 
            "email": "test@example.com", 
            'password': 'hello' 
        }
    ]
value_str = "{ 'email': 'test@example.com', 'password': 'test', 'user_info': { 'name': 'Test user', 'email': 'test@example.com', 'list': [ (1, 2, '3'), 12.5 ] } }"
value_str2 = "Hello World!"
value_bytes = "{ 'email': 'test@example.com', 'password': 'test', 'user_info': { 'name': 'Test user', 'email': 'test@example.com' } }"
value_bytes2 = b"hello world"
value_tuple = ( 
        { 
            "email": "test@example.com", 
            'password': 'hello' ,
            "user_info": {
                "name": "Test user",
                "email": "test@example.com",
                "password": "test",
            },
            'ABCDEF': ('Good','Morning','Teacher')
        }, 
        9999.10, 
        ['HELLO'] 
    )
value_int = 123456
value_float = 12.345
value_custom = {
    "email": "test@example.com",
    "password": "test",
    "list": [
        "Hello", 
        1234, 
        6.6789, 
        ['A','B'], 
        10.123, 
        { 
            "email": "test@example.com", 
            'password': 'hello' 
        }
    ],
    "user_info": {
        "name": "Test user",
        "user_info": {
            "name": "Test user",
            "email": "test@example.com",
            "password": "test",
        },
        "email": "test@example.com",
        "password": "test"
    },
    "tuple": ( 
        { 
            "email": "test@example.com", 
            'password': 'hello' ,
            "user_info": {
                "name": "Test user",
                "email": "test@example.com",
                "password": "test",
            }
        }, 
        9999.10, 
        ['HELLO'] 
    )
}


def data_transform_factory(data):
    obj = None
    if isinstance(data, list):
        obj = ListDataTransform(data)
    elif isinstance(data, str):
        obj = StringDataTransform(data)
    elif isinstance(data, bytes):
        obj = StringDataTransform(data.decode())
    elif isinstance(data, dict):
        obj = DictDataTransform(data)
    elif isinstance(data, tuple):
        obj = TupleDataTransform(data)
    elif isinstance(data, int):
        obj = data
    elif isinstance(data, float):
        obj = data
    else:
        raise ValueError('Invalid data!')
    
    return obj


def data_transform(data):
    obj = data_transform_factory(data)
    if hasattr(obj, 'transform'):
        return obj.transform()
    else:
        return obj


class DictDataTransform():
    def __init__(self, data):
        self._data = data
    
    def transform(self):
        new_dict = {}
        for k, v in self._data.items():
            if isinstance(v, dict):
                self._data = v
                v = self.transform()
            if isinstance(v, list):
                new_dict[k] = ListDataTransform(v).transform()
            if isinstance(v, tuple):
                new_dict[k] = TupleDataTransform(v).transform()
            
            if not k == "password" and not isinstance(v, (list,tuple)):
                new_dict[k] = v
            if k == "email":
                new_dict[k] = "redacted"

        return new_dict


class ListDataTransform():
    def __init__(self, data):
        self._data = data

    def transform(self):
        new_list = []
        for v in self._data:
            if isinstance(v, list):
                self._data = v
                new_list.append(self.transform())
            elif isinstance(v, dict):
                new_list.append(DictDataTransform(v).transform())
            elif isinstance(v, tuple):
                new_list.append(TupleDataTransform(v).transform())
            else:
                new_list.append(v)

        return new_list


class TupleDataTransform():
    def __init__(self, data):
        self._data = data

    def transform(self):
        new_tuple = []
        for v in self._data:
            if isinstance(v, tuple):
                self._data = v
                new_tuple.append(self.transform())
            elif isinstance(v, dict):
                new_tuple.append(DictDataTransform(v).transform())
            elif isinstance(v, list):
                new_tuple.append(ListDataTransform(v).transform())
            else:
                new_tuple.append(v)
    
        return tuple(new_tuple)


class StringDataTransform():
    def __init__(self, data):
        self._data = data

    def transform(self):
        try:
            self._data = eval(self._data)
            return DictDataTransform(self._data).transform()
        except SyntaxError:
            return self._data


def main():
    print(data_transform(value))


if __name__ == '__main__':
    main()