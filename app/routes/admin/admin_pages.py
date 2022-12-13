from app import app, render_template, redirect

from flask_login import current_user
from app.modules.models import *
from app.modules.images_tools import *


@app.route('/admin/login')
def admin_login_page(error_code: int = 100):  # dev: Code 100 is OK code
    return render_template('admin/login_page.html')


@app.route('/admin/dashboard')
def admin_dashboard_page():
    if not current_user.is_authenticated:
        return redirect('/admin/login')

    images = get_images()
    data = {
        'images': {
            'total': len(images),
            'unique_ip': len(get_unique_ips(images))
        }
    }
    return render_template('admin/dashboard_page.html', data=data)
