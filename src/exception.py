'''The sys module in Python provides various functions and variables that are used to manipulate 
different parts of the Python runtime environment. It allows operating on the interpreter as it provides
access to the variables and functions that interact strongly with the interpreter.'''
import sys
from src.logger import logging

# error_detail is present in sys that is why we have written "error_detail:sys"
def error_message_detail(error,error_detail:sys):

    # _,_ becasue i am not interested in the first 2 information
    # exc_tb will tell us in which file and line the exception has occurred
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,
        exc_tb.tb_lineno,
        str(error))
    
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
