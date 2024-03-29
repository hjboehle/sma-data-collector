"""module arguments.arguments"""

import argparse
import logging
from logger.config_logger import configure_logger


logger = logging.getLogger(__name__)


def parse_arguments(args=None) -> argparse.Namespace:
    """
    Parses command-line arguments for the Modbus TCP client.
    
    This function parses the command-line arguments and returns a dictionary containing the 
    parsed arguments.
    
    Returns:
        An object from the class argparse.Namespace.
    """
    logger.info("success: parsing the arguments has started")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--ip_address",
        "-i",
        type=str,
        required=True,
        help="The IP address of the MODBUS server"
    )
    parser.add_argument(
        "--log_level",
        "-l",
        type=str,
        required=False,
        choices=[
            "CRITICAL",
            "ERROR",
            "WARNING",
            "INFO",
            "DEBUG",
        ],
        help="The debug level of the logging outputs"
    )
    logger.info("success: arguments %s parsed and returned", parser.parse_args(args))
    return parser.parse_args(args)


if __name__ == "__main__":
    configure_logger(log_level="INFO")
    logger.info("note: this file '%s' can not run directly", __file__)
