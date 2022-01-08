# LINE MAN Wongnai Intern Assignment
## Software Engineer, Backend (Python)

Author: [Wachirawitch Yuangwipak](https://www.wachirawitch.works/)  
Contact me: [wachirawitch@kkumail.com](mailto:wachirawitch@kkumail.com)

### Usage
```
python app.py
```

### Initial value
```python
value = {
    "email": "test@example.com",
    "password": "test",
    "user_info": {
        "name": "Test user",
        "email": "test@example.com",
    },
}
```
### Output
```
{'email': 'redacted', 'user_info': {'name': 'Test user', 'email': 'redacted'}}
```

### Custom value
I've added some custom values to the 'custom_values' region. You need to remove comment out and then call and print the data_transform(`custom_value`) function.
```python
value_custom = {
    'data': [
         {
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
                        "age": 21,
                    }
                }, 
                9999.10, 
                ['HELLO'] 
            )
        } 
    ]
}
```

### Output
```
{'data': [{'email': 'redacted', 'list': ['Hello', 1234, 6.6789, ['A', 'B'], 10.123, {'email': 'redacted'}], 'user_info': {'name': 'Test user', 'user_info': {'name': 'Test user', 'email': 'redacted'}, 'email': 'redacted'}, 'tuple': ({'email': 'redacted', 'user_info': {'name': 'Test user', 'email': 'redacted', 'age': 21}}, 9999.1, ['HELLO'])}]}
```