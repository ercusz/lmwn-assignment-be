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
value_str = "12345"
value_bytes = b"hello world"
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

output = {
    'email': 'redacted', 
    'list': [
        'Hello', 
        1234, 
        6.6789, 
        ['A', 'B'], 
        10.123, 
        {
            'email': 'redacted'
        }
    ], 
    'user_info': {
        'name': 'Test user', 
        'user_info': {
            'name': 'Test user', 
            'email': 'redacted'
        }, 
        'email': 'redacted'
    }, 
    'tuple': (
        {
            'email': 'redacted', 
            'user_info': {
                'name': 'Test user', 
                'email': 'redacted'
            }
        }, 
        9999.1, 
        ['HELLO']
    )
}

def type_decision(data):
    if isinstance(data, list):
        return transform_list_data(data)
    elif isinstance(data, str):
        return data
    elif isinstance(data, bytes):
        return data.decode()
    elif isinstance(data, dict):
        return transform_dict_data(data)
    elif isinstance(data, tuple):
        return transform_tuple_data(data)
    elif isinstance(data, int):
        return data
    elif isinstance(data, float):
        return data
    else:
        return "Invalid data type"

def transform_dict_data(data):
    new_dict = {}
    for k, v in data.items():
        if isinstance(v, dict):
            v = transform_dict_data(v)
        if isinstance(v, list):
            new_dict[k] = transform_list_data(v)
        if isinstance(v, tuple):
            new_dict[k] = transform_tuple_data(v)
        
        if not k == "password" and not isinstance(v, (list,tuple)):
            new_dict[k] = v
        if k == "email":
            new_dict[k] = "redacted"

    return new_dict

def transform_list_data(data):
    new_list = []
    for v in data:
        if isinstance(v, list):
            new_list.append(transform_list_data(v))
        elif isinstance(v, dict):
            new_list.append(transform_dict_data(v))
        elif isinstance(v, tuple):
            new_list.append(transform_tuple_data(v))
        else:
            new_list.append(v)

    return new_list

def transform_tuple_data(data):
    new_tuple = []
    for v in data:
        if isinstance(v, tuple):
            new_tuple.append(transform_tuple_data(v))
        elif isinstance(v, dict):
            new_tuple.append(transform_dict_data(v))
        elif isinstance(v, list):
            new_tuple.append(transform_list_data(v))
        else:
            new_tuple.append(v)
    
    return tuple(new_tuple)

def main():
    #print(transform_dict_data(value_custom))
    # list, str, bytes, dict, tuple, int, float
    print(type_decision(value_custom))


if __name__ == '__main__':
    main()