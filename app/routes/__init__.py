from app import app, render_template


@app.route('/')
def index_page():
    content_data = {
        'headers': ['My web-site', 'GitHub'],
        'header_links': ['https://hacknet-dev.tech/', 'https://github.com/Konstantin-create/']
    }
    return render_template('index_page.html', content_data=content_data)
