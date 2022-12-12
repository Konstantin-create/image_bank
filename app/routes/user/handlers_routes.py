from app.modules.images_tools import *
from app import app, request, redirect


@app.route('/add/image', methods=['GET', 'POST'])
def add_image_handler():
    if request.method == 'POST':
        image = request.files['image']
        if not image:
            return redirect('/')

        current_id = get_last_id() + 1
        image.save(f'app/static/data/image-{current_id}.jpg')

        add_image(f'app/static/data/image-{current_id}.jpg', request.remote_addr)
        return redirect(f'/image/{current_id}')
