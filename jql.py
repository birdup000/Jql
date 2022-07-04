import json
import os
import re
import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class jql:
    def __init__(self, sqlFile, sep = '.'):
        self.sqlFile = sqlFile
        self.sep = sep
        self.connection = sqlite3.connect(self.sqlFile)
        self.cursor = self.connection.cursor()

        self.connection.row_factory = dict_factory
    
    def read(self, path):
        split = path.split(self.sep)
        get = self.connection.execute(f"SELECT * FROM main WHERE key = '{split[0]}'").fetchall()
        if len(get) == 0:
            return {}        
        get = get[0]
        
        if "value" in get:
            split = split[1:]

            js = json.loads(get["value"])


            for i in range(len(split)):
                if split[i] in js:
                    js = js[split[i]]
                else:
                    return None
            return js
        
        return get
    
    def get_all(self):
        return self.connection.execute("SELECT * FROM main").fetchall()

    def write(self, path, value):
        main_split = path.split(self.sep)
        get = self.connection.execute(f"SELECT * FROM main WHERE key = '{main_split[0]}'").fetchall()
        if get != []:
            get = get[0]
        else:
            get = {}
            get["key"] = ""
            get["value"] = "{}"

        split = main_split[1:]

        main_json = json.loads(get["value"])

        js = main_json
        for i in range(len(split)-1):
            if split[i] in js:
                js = js[split[i]]
            else:
                js[split[i]] = {}
                js = js[split[i]]
        if split == []:
            js[value] = ""
        else:
            js[split[-1]] = value
        self.set_value_raw(main_split[0], json.dumps(main_json))
        return main_json


    def delete(self, path):
        main_split = path.split(self.sep)
        get = self.connection.execute(f"SELECT * FROM main WHERE key = '{main_split[0]}'").fetchall()[0]
        if "value" in get:
            split = main_split[1:]

            main_json = json.loads(get["value"])

            js = main_json
            for i in range(len(split)-1):
                if split[i] in js:
                    js = js[split[i]]
                else:
                    js[split[i]] = {}
                    js = js[split[i]]
            del js[split[-1]]
            self.set_value_raw(main_split[0], json.dumps(main_json))
            return main_json
        
        return get
    
    def set_value_raw(self, key, value):
        get = self.connection.execute(f"SELECT * FROM main WHERE key = '{key}'").fetchall()
        if get == []:
            self.connection.execute("INSERT INTO main VALUES (?, ?)", (key, value))
        else:
            self.connection.execute(f"UPDATE main SET value = '{value}' WHERE key = '{key}'")
        self.save()
    
    def rename_key(self, key, new_key):
        self.connection.execute(f"UPDATE main SET key = '{new_key}' WHERE key = '{key}'")
        self.save()
    
    def delete_key(self, key):
        self.connection.execute(f"DELETE FROM main WHERE key = '{key}'")
        self.save()
    
    def db_exist(self):
        return os.path.isfile(self.sqlFile)
    
    def create_db(self):
        self.update('')

        
    def save(self):
        self.connection.commit()
    
    def __exit__(self):
        self.connection.close()
        
    
    def create_table(self, tableName, columns):
        sql = 'CREATE TABLE ' + tableName + '('
        for i in range(len(columns)):
            sql += columns[i]
            if i < len(columns) - 1:
                sql += ', '
        sql += ');'
        self.update(sql)


if __name__ == "__main__":
    test = jql("my_database.db")
    test.read("dfsaafasdf")

#test.write("eiko", 1465)
#test.write("eikosa.password","1234")
#test.write("eikosa.age","82")
#
#test.write("eikosa.books.technic.python","")
#test.write("eikosa.books.technic.physics","")

#test.write("eikosa.books.literature.dosteyovsky","")

#test.delete("eikosa.books.literature.tolstoy")

#test.read("eikosa.books.literature")
