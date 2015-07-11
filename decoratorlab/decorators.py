"""
Examples of decorators
"""


def identity_decorator(decorated_func):
    """
    Does nothing, passes the decorated function straight through.

    If you wanted to do some thing like log the time the function
    was called you could do that before the function returned.
    """
    return decorated_func

def double_decorator(decorated_func):
    """
    Doubles the result of the original function call
    """
    def replacement_function(_int):
        # apply the decorated function to its arguments
        interim_result = decorated_func(_int)
        # now wrap that result with the decorator's functionality
        # in this case a doubling.
        final_result = 2 * interim_result
        return final_result
    return replacement_function

def parameterized_decorator(_param):
    """
    This decorator is actually a function which generates a decorator
    not a decorator itself.

    Thus, we have two levels of inner functions to define.
    The first returns the newly minted decorator which is a function
    which takes the decorated function in the calling code.
    The second is the implementation of the decorating function itself.
    """
    def decorator(decorated_func): 
         """
         The parameter is expected to be an integer
         """
         def replacment_function(_int):
             interim_result = decorated_func(_int) 
             final_result = _param * interim_result  
             return final_result
         return replacment_function
    return decorator
