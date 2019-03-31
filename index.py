"""Main Lambda handler."""

import json
import logging


def handler(event, _context):
    """Handle Lambda events."""
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.info("Serving CS Coffee Chat request!")
    return {
        'statusCode': 200,
        'body': json.dumps("Submission successful!")
    }
