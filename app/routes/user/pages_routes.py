from app.modules.images_tools import *
from app.modules.content_tools import *
from app.modules.statistics_tools import add_image_view
from app import app, render_template, request, send_file, redirect


@app.route('/')
def index_page():
    return render_template('user/index_page.html', content_data=get_content())


@app.route('/image-manager/<int:image_id>')
def image_manager_page(image_id: int):
    image = get_image(image_id)
    if not image:
        return redirect('/not-found')
    return render_template(
        'user/image_manager_page.html',
        image=image,
        content_data=get_content(),
        your_image=request.remote_addr == image.from_ip,
        server_ip=request.host
    )


@app.route('/img/<int:image_id>')
def image_page(image_id: int):
    image = get_image(image_id)
    if not image:
        return redirect('/not-found')

    add_image_view(image_id, request.remote_addr)
    return send_file(f'static/data/image-{image_id}.jpg', mimetype='image/jpg')


@app.route('/not-allowed')
def not_allowed_page():
    return render_template('user/not_allowed_page.html', content_data=get_content())


@app.route('/not-found')
def not_found_page():
    return render_template('user/not_found_page.html', content_data=get_content())
