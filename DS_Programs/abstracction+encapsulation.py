class Database:
    def __init__(self):
        self.__storage ={}  #private
        #self.storage  = {} #public
        #self._storage = {} #protected

    def save_data(self, key, value):
        self.__storage[key] = value
        print(f"Data saves for {key}")

    def get_data(self, key):
        return self.__storage.get(key, "No data found")
    
db = Database()
db.save_data("User_101", {"name": "Raj", "age": 30})
print(db.get_data("user_101"))
