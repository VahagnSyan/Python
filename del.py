'''
In this module I have function dell
'''


VARIABLE = 10


def dell(obj: str):
    '''
    My variant for del keyword
    '''
    try:
        globals().pop(obj)
    except KeyError as ke:
        raise NameError(f"name '{obj}' is not defined") from ke


dell('VARIABLE')
