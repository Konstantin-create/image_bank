import json


def get_content() -> dict:
    """Function to get content from content.json file"""

    return json.load(open('app/data/content.json', 'r'))
