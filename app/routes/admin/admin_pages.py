from app import app, render_template, redirect

from flask_login import current_user
from app.modules.models import *

from sqlalchemy import func
from sqlalchemy.sql import label


@app.route('/admin/login')
def admin_login_page(error_code: int = 100):  # dev: Code 100 is OK code
    return render_template('admin/login_page.html')


@app.route('/admin/dashboard')
def admin_dashboard_page():
    if not current_user.is_authenticated:
        return redirect('/admin/login')

    images = Image.query.all()
    unique_ips = set()
    for image in images:
        unique_ips.add(image.from_ip)

    data = {
        'images': {
            'total': len(images),
            'unique_ip': len(unique_ips)
        }
    }
    return render_template('admin/dashboard_page.html', data=data)
