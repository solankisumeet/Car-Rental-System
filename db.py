from tinydb import TinyDB, where
from tinydb.queries import Query
import os

class rentaldb():
    
    def __init__(self) -> None:
        self.data_db = TinyDB("carrentaldb.json")
        self.user = self.data_db.table("users")
        
        
    def get_user(self, uname):
        return self.user.search(Query().username == uname)
    
    def save_user(self, save_data):
        self.user.insert(save_data)