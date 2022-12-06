from app import app, render_template


@app.route('/')
def index_page():
    return render_template('index_page.html')
