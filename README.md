# JQL ⚙️

It combines SQL's speed and JSON's flexibility.

SQL + JSON = JQL ⚙️

By _Eiko_

All JQL tables have two columns, Key and Value, value is json.

![image](https://user-images.githubusercontent.com/20538090/168511649-75ca7a7a-8670-42b0-86b9-a0d0acda6f45.png)

## 📚 Examples

### ✏️ Write
```jql("my_database.db").write("eikosa.books.literature.Dostoyevsky","")```


Value is:
```
{
    "books": {
        "literature": {
            "Dostoyevsky": ""
        }
    }
}
```



```jql("my_database.db").write("eikosa.books.literature.tolstoy","")```

Returns:
```
{
    "books": {
        "literature": {
            "Dostoyevsky": "",
            "tolstoy": ""
        }
    }
}
```

### 📖 Read
```jql("my_database.db").read("eikosa.books.literature")```

Returns:
```
{'Dostoyevsky': ''}
```


### 🗑 Delete Path Element
```jql("my_database.db").del("eikosa.books.literature.tolstoy")```

Before:
```
{
    "books": {
        "literature": {
            "Dostoyevsky": "",
            "tolstoy": ""
        }
    }
}
```
After:
```
{
    "books": {
        "literature": {
            "Dostoyevsky": ""
        }
    }
}
```


```jql("my_database.db").del("eikosa.books.literature")```

Before:
```
{
    "books": {
        "literature": {
            "Dostoyevsky": "",
            "tolstoy": ""
        }
    }
}
```
After:
```
{
    "books": {}
}
```

### 💥 Delete Value
```
jql("my_database.db").delete_key("eikosa")
```
![image](https://user-images.githubusercontent.com/20538090/168512470-0fe16e53-c669-4a02-8386-76f6fd21db36.png)
