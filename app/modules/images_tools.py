from app import db
from app.modules.models import Image


def get_last_id() -> int:
    """Function to return last image id"""

    return Image.query.order_by(Image.id.desc()).first().id


def get_image(image_id: int) -> Image:
    """Function to return image obj"""

    return Image.query.get(image_id)


def add_image(image_path: str, from_ip: str) -> bool:
    """Function to add image"""

    try:
        image = Image(image_path=image_path, from_ip=from_ip)

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
