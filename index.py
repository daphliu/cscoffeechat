"""Main Lambda handler."""

import json
import logging

from google_sheet import FormResult, save_form_result


def handler(event, _context):
    """Handle Lambda events."""
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.info("Serving CS Coffee Chat request!")
    form_encoded = event['queryStringParameters']
    logger.info(f"{form_encoded}")
    form_result = FormResult(
        email=form_encoded['email'],
        name=form_encoded['name'],
        gender=form_encoded['gender'],
        year=form_encoded['year'],
        self_intro=form_encoded['self-intro'],
        non_tech_topic=form_encoded['non-tech-interests'],
        tech_topic=form_encoded['tech-interests'],
        other_preferences=form_encoded['other-prefs']
    )

    try:
        save_form_result(form_result)
    except Exception:
        logging.info(f"Request failed: {event}")
        return {
            'statusCode': 500,
            'body': json.dumps("Oops, something went wrong! Please retry!")
        }

    logging.info("Request successful")
    return {
        'statusCode': 200,
        'body': json.dumps("Submission successful!")
    }
