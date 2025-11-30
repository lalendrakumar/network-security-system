import sys
import logging

def get_error_message(error_message, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    message = f"Error occurred in Script: [{file_name}] at Line: [{line_number}] → {error_message}"
    return message

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = get_error_message(error_message, error_detail)

    def __str__(self):
        return self.error_message
    
if __name__ == "__main__":
    try:
        logging.info("We are inside try block.")
        a = 1 / 0
    except Exception as e:
        raise NetworkSecurityException(str(e), sys) from e

