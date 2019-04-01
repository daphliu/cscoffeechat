"""Interface to Google Sheets."""
from oauth2client.client import GoogleCredentials
from googleapiclient import errors
from googleapiclient.discovery import build
from typing import List, NamedTuple
import httplib2

SPREADSHEET_ID = '1ejbnTskarzX0VgJonjn2wGrdOmKV4k-75itr4mPLcQU'
RANGE_NAME = ''

credentials = create_credentials() 
http = credentials.authorize(httplib2.Http())
credentials.refresh(http)
service = build('sheets', 'v4', http=http)

def create_credentials():
    credentials = GoogleCredentials.get_application_default()
    scope = ['https://www.googleapis.com/auth/drive']
    return credentials.create_scoped(scope)

class FormResult(NamedTuple):
    """Class representing data users enter into coffee chat form."""

    email: str
    name: str
    gender: str
    year: str
    self_intro: str
    non_tech_topic: List[str]
    tech_topic: List[str]
    gender_preference: str
    other_preferences: str


def save_form_result(form_result):
    """Save form result to Google Sheets."""
    try: 
        values = [list(form_result)]
        body = {
            'values': values
        }
        result = service.spreadsheets().values.append(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE_NAME,
            valueInputOption="RAW",
            body=body_
        ).execute()

    except: 
        raise Exception('Oh no, something terrible happened.')
