# app/core/logger.py

import logging

def setup_logging():
    """Configure the logging format and level."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

