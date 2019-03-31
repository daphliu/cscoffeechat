from typing import List, NamedTuple  
 
SPREADSHEET_ID = '...'
RANGE_NAME = '...'

class FormResult(NamedTuple): 
    '''Class representing data users enter into coffee chat form '''
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
    values = [list(form_result)]

    body = {
        'values' : values 
    }

    result = service.spreadsheets().values.append(
        spreadsheetId = SPREADSHEET_ID, 
        range = RANGE_NAME, 
        valueInputOption = "RAW",
        body = body
    ).execute()
    