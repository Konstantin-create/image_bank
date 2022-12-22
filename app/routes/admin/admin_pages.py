from app import app, render_template, redirect

from flask_login import current_user
from app.modules.images_tools import *
from app.modules.statistics_tools import *


@app.route('/admin/login')
def admin_login_page(error_code: int = 100):  # dev: Code 100 is OK code
    """Function of login page handler"""

    return render_template('admin/login_page.html')


@app.route('/admin/dashboard')
def admin_dashboard_page():
    """Function of dashboard page handler"""

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
            'total': get_images_amount(),
            'images_size': get_images_size()
        }
    }
    return render_template('admin/dashboard_page.html', data=data)


@app.route('/admin/images')
def admin_images_page():
    """Function of images page handler"""

    if not current_user.is_authenticated:
        return redirect('/admin/login')

    images = get_images()

    return render_template('admin/images_page.html', images=images)


@app.route('/not-allowed')
def admin_not_allowed_page():
    """Function of not allowed page handler"""

    content_data = {
        'headers': ['My web-site', 'GitHub'],
        'header_links': ['https://hacknet-dev.tech/', 'https://github.com/Konstantin-create/']
    }
    return render_template('user/not_allowed_page.html', content_data=content_data)
