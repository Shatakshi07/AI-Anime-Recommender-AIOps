import sys

class CustomException(Exception): #CustomException is called when we want to raise an exception in our code. It inherits from the built-in Exception class, which means it can be used like any other exception in Python.
    def __init__(self, message: str, error_detail:Exception=None):
        self.error_message=self.get_detailed_error_message(message, error_detail)
        super().__init__(self.error_message)


    # @staticmethod is a built-in decorator used to define a method inside a class that does not access or modify any class-specific or instance-specific state. It behaves exactly like a plain, normal function but lives inside the class's namespace for better code organization and grouping.
    
    @staticmethod 
    def get_detailed_error_message(message, error_detail):
        _, _, exc_tb = sys.exc_info()     #exception type, exception value, exception traceback (exc_tb) -> filename, line no.
        filename = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

        return (
            f"{message} |"
            f"Error: {error_detail} |"
            f"File: {filename} |"
            f"Line: {line_number}"
        )
    
    def __str__(self):
        return self.error_message # when we print the object of CustomException, it will return the error_message instead of the default string representation of the exception.
        # __str__() is magic method. When we do print(__str__()) it will also store the  exception log in the error_message variable and return it when we print the object of CustomException.

"""
Example usecase:


from src.common.custom_exception import CustomException

try:
    a = 1 / 0
except Exception as e:
    raise CustomException("An error occurred while dividing by zero", e)

"""