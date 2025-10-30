from flask import Blueprint, render_template, session, redirect, url_for
from . import db
from .models import User
from .forms import NameForm
from .email import send_simple_message

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False

            admin = main.app.config.get('FLASKY_ADMIN')
            print('Verificando variáveis de ambiente...', flush=True)
            print('FLASKY_ADMIN:', admin, flush=True)

            if admin:
                send_simple_message(
                    [admin, "flaskaulasweb@zohomail.com"],
                    'Novo usuário',
                    form.name.data
                )
        else:
            session['known'] = True

        session['name'] = form.name.data
        return redirect(url_for('main.index'))

    users_list = User.query.order_by(User.username).all()
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False), users=users_list)
