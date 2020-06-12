# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, item_list):
        self.name = name
        self.description = description
        self.item_list=item_list
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
           
    
    def __str__(self):
         output = f"{self.name}. {self.description}. Items in room inventory:\n"
         index=1
         # for item in self.item_list:
         #        if self.item_list is not None:
         #            output += f"{index}. {item.name}, --> quantity:{item.quantity}\n"
         #            index += 1
         if self.s_to:
            output += 'The South is: ' + self.s_to.name + '\n'
         if self.n_to:
            output += 'The North is: ' + self.n_to.name + '\n'
         if self.e_to:
            output += 'The East is: ' + self.e_to.name + '\n'
         if self.w_to:
            output += 'The West is: ' + self.w_to.name + '\n'
         return output


    def add_Item(self,item):
           self.item_list.append(item);
   

    def remove_Item(self,item):
           removed = self.item_list.remove(item)
           return removed


    def get_item(self):
        print(self.item_list)

         
      
           
      
       
    

    
