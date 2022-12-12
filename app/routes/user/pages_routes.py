from app.modules.images_tools import *
from app.modules.statistics_tools import add_image_view
from app import app, render_template, request, send_file

content_data = {
    'headers': ['My web-site', 'GitHub'],
    'header_links': ['https://hacknet-dev.tech/', 'https://github.com/Konstantin-create/']
}


@app.route('/')
def index_page():
    return render_template('user/index_page.html', content_data=content_data)


@app.route('/image-manager/<int:image_id>')
def image_manager_page(image_id: int):
    image = get_image(image_id)
    if not image:
        return '404'
    return render_template(
        'user/image_manager_page.html',
        image=image,
        content_data=content_data,
        your_image=request.remote_addr == image.from_ip,
    )


@app.route('/img/<int:image_id>')
def image_page(image_id: int):
    image = get_image(image_id)
    if not image:
        return '404'

    add_image_view(image_id, request.remote_addr)
    return send_file(f'static/data/image-{image_id}.jpg', mimetype='image/jpg')
