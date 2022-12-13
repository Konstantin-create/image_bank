from app import app_folder

import json
from datetime import datetime


def get_image_stat() -> list:
    """Function to get image statistics"""

    try:
        return json.load(open(f'{app_folder}/data/images_requests.json'))
    except:
        return []


def set_image_stat(new_data: list) -> None:
    """Function to add image statistics"""

    try:
        json.dump(new_data, open(f'{app_folder}/data/images_requests.json', 'w'), indent=2)
    except:
        pass


def add_image_stat(new_data: dict) -> None:
    """Function to add item to statistics"""

    current_stat = get_image_stat()
    current_stat.append(new_data)
    set_image_stat(current_stat)


def add_image_view(image_id: int, view_ip: str) -> None:
    """Function to add view to stat file"""

    data = {
        'image': image_id,
        'view_ip': view_ip,
        'time_stamp': datetime.utcnow().strftime("%Y-%m-%d %H:%M")
    }
    add_image_stat(data)


def clear_image_stat() -> None:
    """Function to clear image statistics"""

    set_image_stat([])
