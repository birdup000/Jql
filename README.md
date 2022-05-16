# JQL

It combines SQL's speed and JSON's flexibility.

SQL + JSON = JQL

All JQL tables have two columns, Key and Value, value is json.

## Examples

### Write
```jql("my_database.db").write("eikosa.books.literature.dosteyovsky","")```

![image](https://user-images.githubusercontent.com/20538090/168511649-75ca7a7a-8670-42b0-86b9-a0d0acda6f45.png)

Value is:
```
{
    "books": {
        "literature": {
            "dosteyovsky": ""
        }
    }
}
```

###Read
```jql("my_database.db").read("eikosa.books.literature")```

Returns:
```
{'dosteyovsky': ''}
```
