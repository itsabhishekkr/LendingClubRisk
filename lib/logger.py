import logging
import sys
import os

def get_logger(name, level=logging.INFO):
    """
    Returns a logger configured with a standard format.
    Simulates a Log4j style layout.
    """
    logger = logging.getLogger(name)
    
    # Avoid duplicate handlers if the logger is already configured
    if not logger.handlers:
        logger.setLevel(level)
        
        # Standard format: TIMESTAMP - LEVEL - NAME - MESSAGE
        format_str = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
        formatter = logging.Formatter(format_str)
        
        # Console Handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        # Optional: File Handler
        # log_file = 'project.log'
        # file_handler = logging.FileHandler(log_file)
        # file_handler.setFormatter(formatter)
        # logger.addHandler(file_handler)
        
    return logger

# Example usage
if __name__ == "__main__":
    test_logger = get_logger("TestLogger")
    test_logger.info("This is an info message")
    test_logger.warning("This is a warning message")
    test_logger.error("This is an error message")
