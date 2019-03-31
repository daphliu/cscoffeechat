"""Main Lambda handler."""

import logging


def handler(event, context):
    """Handle Lambda events."""
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.info("Started CS Coffee Chat!")
