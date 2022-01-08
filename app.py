#   LINE MAN Wongnai Intern - Software Engineer, Backend (Python)
#   Python 3.8
#   Author: Wachirawitch Y. <wachirawitch@kkumail.com>

########################## Problem ##############################
#  [x] find dict with key="email" then set value = "redacted"   #
#  [x] find dict with key="password" then remove it!            #
#  [x] allowed type = list, str, bytes, dict, tuple, int, float #
#################################################################


value = {
    "email": "test@example.com",
    "password": "test",
    "user_info": {
        "name": "Test user",
        "email": "test@example.com",
    },
}
#region custom_values
'''
#   Some of the values I think are covered by the requirements.
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
value_str3 = "['H','I', (10,20.5,30), {'email': 'abc@def.gh', 'password': '113245'}]"
value_str4 = "('H','I', (10,20.5,30), {'email': 'abc@def.gh', 'password': '113245'})"
value_bytes = b"{ 'email': 'test@example.com', 'password': 'test', 'user_info': { 'name': 'Test user', 'email': 'test@example.com' } }"
value_bytes2 = b"hello world"
value_bytes3 = b"['H','I', (10,20.5,30), {'email': 'abc@def.gh', 'password': '113245'}]"
value_bytes4 = b"('H','I', (10,20.5,30), {'email': 'abc@def.gh', 'password': '113245'})"
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
    'data': 
        [ {
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
        } ]
}
'''
#endregion 


#   I implemented 'Factory Method' pattern for this work.
#   The function below I use to decide what kind of 
#   transformation function should be used for the input data type.
def data_transform_factory(data):
    obj = None
    if isinstance(data, list):
        obj = ListDataTransform(data)
    elif isinstance(data, str):
        obj = StringDataTransform(data, False).transform()
        if isinstance(obj, str):
            return obj
        else:
            return data_transform_factory(obj)
    elif isinstance(data, bytes):
        obj = StringDataTransform(data, True).transform()    #   decode bytes to str before use a function
        if isinstance(obj, bytes):
            return obj
        else:
            return data_transform_factory(obj)
    elif isinstance(data, dict):
        obj = DictDataTransform(data)
    elif isinstance(data, tuple):
        obj = TupleDataTransform(data)
    elif isinstance(data, int):
        obj = data          #   no tranformation function for int/float data
                            #   because I think dict data is can't be contained inside of int/float data
                            #   unless it has passed the encoding function.
    elif isinstance(data, float):
        obj = data
    else:
        raise ValueError('Invalid data!')
    
    return obj


#   The function below I use to create a factory object
#   and call the 'transform' method
def data_transform(data):
    obj = data_transform_factory(data)
    if hasattr(obj, 'transform'):   # check the obj has a transform method or not
        return obj.transform()
    else:
        return obj


#   This class for data 'type=dict'
class DictDataTransform():
    def __init__(self, data):
        self._data = data
    
    def transform(self):
        new_dict = {}   #   empty dict for assign a new data and then return to caller
        for k, v in self._data.items(): #   dictionary iteration
            if isinstance(v, dict):
                self._data = v          #  set new self._data to current value
                v = self.transform()    #  recursion
            if isinstance(v, list):
                new_dict[k] = ListDataTransform(v).transform()  #  call list transformation & assign to new_dict with current key
            if isinstance(v, tuple):
                new_dict[k] = TupleDataTransform(v).transform() #  call tuple transformation & assign to new_dict with current key
            
            # The 2 conditions below are used to decide which data should be in new_dict
            if not k == "password" and not isinstance(v, (list,tuple)):
                new_dict[k] = v
            if k == "email":
                new_dict[k] = "redacted"

        return new_dict


#   This class for data 'type=list'
class ListDataTransform():
    def __init__(self, data):
        self._data = data

    def transform(self):
        new_list = []   #   empty list for assign a new data and then return to caller
        for v in self._data:    #   list iteration
            if isinstance(v, list):
                self._data = v                      #  set new self._data to current value
                new_list.append(self.transform())   #  recursion
            elif isinstance(v, dict):
                new_list.append(DictDataTransform(v).transform())   #  call dict transformation & append to new_list
            elif isinstance(v, tuple):
                new_list.append(TupleDataTransform(v).transform())  #  call tuple transformation & append to new_list
            else:
                new_list.append(v)

        return new_list


#   This class for data 'type=tuple'
class TupleDataTransform():
    def __init__(self, data):
        self._data = data

    #   This transformation method is similar to list
    #   but the return state is convert list to tuple
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


#   This class for data 'type=str/bytes'
#   used to convert string/bytes representation of dict to dict
class StringDataTransform():
    def __init__(self, data, isBytes=False):
        self._data = data
        self._isBytes = isBytes #   for checking bytes data

    def transform(self):
        try:
            if (self._isBytes):
                self._data = self._data.decode()
            old_data = self._data
            self._data = eval(self._data, {"__builtins__": None}, {})   #   Use eval() to evaluates a string as a dict
                                                                        #   add some expressions to prevent code execution
                                            #   !!! eval() in python is weak of security !!!
                                            #   PLEASE use alternative choices such as 'json', 'ast.literal_eval'
                                            #   for more information    https://docs.python.org/3/library/json.html
                                            #                           https://docs.python.org/3/library/ast.html
                                            #   But in this work I have limitations on using external modules
            return self._data if isinstance(self._data, (dict, list, tuple)) else old_data
        except SyntaxError:     #   if data isn't represent of dict data return original data
            return self._data.encode() if self._isBytes else self._data


def main():
    print(data_transform(value))


if __name__ == '__main__':
    main()