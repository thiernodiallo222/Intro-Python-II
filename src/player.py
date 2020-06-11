# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    def __str__(self):
        return f"I am {self.name}, and {self.location}"
    
    def __repr__(self):
        return f"self.name = {self.name} ; self.location = {self.location}"
