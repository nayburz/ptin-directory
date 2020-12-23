from django import template
from directory.models import Person

register = template.Library() 

# @TODO Fix or delete. 

@register.filter
def state_initial(value):
    """ 
    Returns the first 2 characters of a state in uppercase for a given state
    """
    state = value.split()[-1] # get the state from value
    return state[1].upper() # get the first letter of last name in lower case