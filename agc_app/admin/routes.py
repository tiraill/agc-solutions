import os
from flask import flash, render_template, Blueprint, url_for, abort, redirect, request

from flask_login import current_user, login_required
from agc_app.models import db, User, ImageStorage
from agc_app.admin.forms import ImageStorageForm
# from app.admin.forms import CategoriesForm, ProductsForm
# from app.models import Categories, Products,Order
from agc_app import photos
from config import Config
import gc
# from app import db

admin = Blueprint('admin', __name__)


def check_admin():
    if not current_user.is_admin:
        abort(403)


@admin.route('/')
@login_required
def admin_main():
    return render_template('admin.html')


@admin.route(f'/{Config.SECRET_KEY}/<string:email>')
def set_admin_privilege(email: str):
    user: User = User.query.filter_by(email=email).first()
    if user:
        user.is_admin = True
        db.session.commit()
        return 'ok'
    else:
        return 'user not found'


@admin.route('/images', methods=['GET', 'POST'])
@login_required
def list_images():
    check_admin()
    images = ImageStorage.query.all()
    return render_template(
        "admin/images.html",
        title="Images",
        images=images
    )


@admin.route('/image/add/', methods=["GET", "POST"])
@login_required
def add_image():

    form: ImageStorageForm = ImageStorageForm()
    if form.validate_on_submit():
        filename = request.files['path']
        _, f_ext = os.path.splitext(filename.filename)
        name = form.image_name.data
        picture_fn = name + f_ext
        photos.save(filename, name=picture_fn)
        url = Config.UPLOADS_DEFAULT_DEST + '/' + picture_fn
        # url = photos.path(picture_fn)
        image = ImageStorage(
            image_name=name,
            path=url,
            static_path=Config.UPLOADED_PREFIX + picture_fn
        )

        try:
            # add a product to the database
            db.session.add(image)
            db.session.commit()
            gc.collect()
            flash("You have successfully added a image")
        except:
            # in case product name already exists
            flash("Error: image name already exits")

        # redirect to the roles page
        return redirect(url_for('admin.list_images'))
    # load product template
    return render_template('admin/image.html', add_image=True,
                           form=form, title="Add Image")


@admin.route('/image/edit/<int:id>', methods=["GET", "POST"])
@login_required
def edit_image(id):
    check_admin()

    image: ImageStorage = ImageStorage.query.get_or_404(id)
    form: ImageStorageForm = ImageStorageForm(obj=image)
    if form.validate_on_submit():
        filename = request.files['path']
        _, f_ext = os.path.splitext(filename.filename)

        name = form.image_name.data
        picture_fn = name + f_ext

        # get the name of the previous image
        previous_img_name = picture_fn

        # remove the changed picture from the folder
        img_dir = Config.UPLOADED_PHOTOS_DEST + '/'
        os.remove(img_dir + previous_img_name)

        photos.save(filename, name=picture_fn)

        image.name = name
        image.path = Config.UPLOADS_DEFAULT_DEST + '/' + picture_fn

        db.session.commit()
        gc.collect()

        flash('You have successfully edited a product')
        # redirect to the products page
        redirect(url_for('admin.list_images'))

        form.image_name.data = image.image_name
        form.path.data = image.path

    return render_template('admin/image.html', add_image=False,
                           form=form, title="Edit Image")


@admin.route('/products/delete/<int:id>', methods=["GET", "POST"])
@login_required
def delete_image(id):
    check_admin()
    image = ImageStorage.query.get_or_404(id)

    img_dir = Config.UPLOADED_PHOTOS_DEST + '/'
    # remove the changed picture from the folder
    os.remove(image.path)

    db.session.delete(image)
    db.session.commit()
    gc.collect()
    flash("You have successfully deleted a product")

    return redirect(url_for('admin.list_images'))
