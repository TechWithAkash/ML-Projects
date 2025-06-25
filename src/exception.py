import sys
from logger import logging
# Funtion to format the error message with file name, line number, and error message
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


# Custom Exception Class are used to raised the coustome exceptions that occured by errors
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    

    # String representation of the CustomException 
    def __str__(self):
        return self.error_message


# Example usage of the CustomException class
if __name__ == "__main__":
    try:
        a = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        logging.error("Divide by zero error occurred...")
        raise CustomException(e,sys) from e


 


