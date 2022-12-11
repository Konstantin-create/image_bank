from app.modules.images_tools import *

from app import db
from app import app, render_template, request, redirect


@app.route('/add/image', methods=['GET', 'POST'])
def add_image():
    if request.method == 'POST':
        image = request.files['image']
        if not image:
            return redirect('/')

        current_id = get_last_id() + 1
        image.save(f'app/static/data/image-{current_id}.jpg')

        image_obj = add_image(image_path=f'app/static/data/image-{current_id}.jpg', from_ip=request.remote_addr)
        db.session.add(image_obj)
        db.session.commit()
        return redirect(f'/image/{current_id}')
    return redirect('/')
