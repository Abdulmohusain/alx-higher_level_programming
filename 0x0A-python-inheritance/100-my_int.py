"""this module contains MyInt class that inherits
from int
"""


class MyInt(int):
    """This defines rougue int data type that always want vawulence
    we have the == operatoer and != operator inverted
    """

    def __eq__(self, other_object):
        """This modifies the == operator to !=
        Args:
            other_object: The object to check if its !=
        """
        return self != other_object
    
    def __ne__(self, other_object):
        """This modifies the == operator to !=
        Args:
            other_object: The object to check if its !=
        """
        return self == other_object

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)


        