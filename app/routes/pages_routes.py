from app import app, render_template
from app.modules.images_tools import *


@app.route('/')
def index_page():
    content_data = {
        'headers': ['My web-site', 'GitHub'],
        'header_links': ['https://hacknet-dev.tech/', 'https://github.com/Konstantin-create/']
    }
    return render_template('index_page.html', content_data=content_data)


@app.route('/image/<int:image_id>')
def image_page(image_id: int):
    image = get_image(image_id)
    if not image:
        return '404'
    return render_template('image.html', image_id=str(image.id))
