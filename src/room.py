# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
           
    
    def __str__(self):
         output = f"Welcome to {self.name}! Description: {self.description}\n"
         if self.s_to:
            output += 'The South is: ' + self.s_to.name + '\n'
         if self.n_to:
            output += 'The North is: ' + self.n_to.name + '\n'
         if self.e_to:
            output += 'The East is: ' + self.e_to.name + '\n'
         if self.w_to:
            output += 'The West is: ' + self.w_to.name + '\n'
         return output
         

    # def __repr__(self):
    #     output = "Welcome to {self.name}! Description: {self.description}\n"
    #     if self.s_to:
    #         output += 'the South is: ' + self.s_to.name + '\n'
    #     if self.n_to:
    #         output += 'the North is: ' + self.n_to.name + '\n'
    #     if self.e_to:
    #         output += 'the East is: ' + self.e_to.name + '\n'
    #     if self.w_to:
    #         output += 'the West is: ' + self.w_to.name + '\n'
    #     return output
       
    

    
