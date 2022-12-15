from app import app, render_template, redirect

from flask_login import current_user
from app.modules.images_tools import *
from app.modules.statistics_tools import *


@app.route('/admin/login')
def admin_login_page(error_code: int = 100):  # dev: Code 100 is OK code
    return render_template('admin/login_page.html')


@app.route('/admin/dashboard')
def admin_dashboard_page():
    if not current_user.is_authenticated:
        return redirect('/admin/login')

    images = get_images()
    data = {
        'requests': {
            'total': len(get_image_stat()),
            'unique_ip': len(get_unique_ips(images)),
            'popular_image': get_most_popular_image(get_image_stat())
        },
        'images': {
            'total': get_images_amount()
        }
    }
    return render_template('admin/dashboard_page.html', data=data)
