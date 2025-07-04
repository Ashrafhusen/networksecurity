import sys  
from networkSecurity.logging import logger 

class NetworkSecurityException(Exception):
    
    def __init__(self, error_message, error_details: sys):
       self.error_message = error_message
       _,_,exc_tb = error_details.exc_info()

       self.lineno = exc_tb.tb_lineno
       self.filename = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occurred in script: {self.filename} at line number: {self.lineno} with message: {self.error_message}"
        self.file_name, self.line_no, str(self.error_message)

if __name__ == "__main__":
    try:
        logger.logging.info("Starting the Network Security Exception module")
        a= 1/0
        print("This will not be printed", a)
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e
