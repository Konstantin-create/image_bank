import os
import glob
from typing import Union

from app import db, app_folder
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
        os.remove(f'{app_folder}/data/image-{image_id}.jpg')
        db.session.delete(image)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False


def get_unique_ips(images: list) -> set:
    """Function to count unique ips"""

    ips = []
    for image in images:
        ips.append(image.from_ip)
    return set(ips)


def get_most_popular_image(images_requests: list) -> str:
    """Function to get the most popular image"""

    if not images_requests:
        return 'no requests at any image'

    images = {}
    for image in images_requests:
        if image['image'] not in images:
            images[image['image']] = 1
        else:
            images[image['image']] += 1

    return f'image-{max(list(images.items()), key=lambda x: x[1])[0]}'


def sizeof_fmt(num, suffix="B"):
    """Function to convert file size in bytes to human-readable string python"""

    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


def get_images_amount() -> int:
    """Function to get amount of images on local storage"""

    return len(glob.glob(f'{app_folder}/static/data/*'))


def get_images_size() -> str:
    """Function to get a size of images on local storage"""

    return sizeof_fmt(sum(d.stat().st_size for d in os.scandir(f'{app_folder}/static/data') if d.is_file()))
