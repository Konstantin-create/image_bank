from app import app, render_template, request, redirect


@app.route('/add/image', methods=['GET', 'POST'])
def add_image():
    if request.method == 'POST':
        image = request.files['image']
        if not image:
            return redirect('/')

