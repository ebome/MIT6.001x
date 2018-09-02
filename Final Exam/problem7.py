'''
All of Python immutable built-in objects are hashable, 
while no mutable containers (such as lists or dictionaries) are. 
Objects which are instances of user-defined classes are hashable by default;
'''
class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        try:
            self.vals[e] -= 1
        except:
            self.vals[e] = 1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        count=0
        super().__init__()
        for elt in self.vals.keys():
            if elt == e:
                count +=1
        return count
    
# partial correct
