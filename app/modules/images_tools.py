from typing import Union

from app import db
from app.modules.models import Image


def get_last_id() -> Union[int, None]:
    """Function to return last image id"""

    if not Image.query.get(1):
        return 0
    return Image.query.order_by(Image.id.desc()).first().id


def get_image(image_id: int) -> Union[Image, None]:
    """Function to return image obj"""

    return Image.query.get(image_id)


def get_images() -> list:
    """Function to get list of all images"""

    return Image.query.all()


def add_image(image_path: str, from_ip: str) -> bool:
    """Function to add image"""

    try:
        image = Image(image_path=image_path, from_ip=from_ip)
        print(image)

        db.session.add(image)
        db.session.commit()
        return True
    except:
        return False


def delete_image(image_id: int) -> bool:
    """Function to delete image"""

    try:
        image = get_image(image_id)
        db.session.delete(image)
        db.session.commit()
        return True
    except:
        return False


def get_unique_ips(images: list) -> set:
    """Function to count unique ips"""

    return set(images)
