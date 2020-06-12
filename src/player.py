# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, item_list):
        self.name = name
        self.current_room = current_room
        self.item_list =item_list
    def __str__(self):
         output = f"I am {self.name}, and this is {self.current_room} I have the following items:"
         index=1
         for item in self.item_list:
                if self.item_list is not None:
                    output += f"\n {index}. {item.name}, --> quantity:{item.quantity} "
                    index += 1
         return output
    

    def add_Item(self,item):
           self.item_list.append(item)


    def remove_Item(self, item):
        removed = self.item_list.remove(item)
        return removed
          


    def get_item(self):
        print(self.item_list)
