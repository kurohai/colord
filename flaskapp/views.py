from flask import Blueprint
from flask import render_template, request, url_for
from dicto import dicto
from sqlalchemy import and_
from pprint import pprint
import codecs
import os
from flaskapp import *


blueprint = Blueprint(flasktemplate.appnamed, __name__)

@blueprint.route('/notemd/', methods=['GET', 'POST'])
@blueprint.route('/notemd/<note>/', methods=['GET', 'POST'])
def notemd(note=None):
    if note is None:
        note = (
            '# Enter your markdown note here.\n'
            '## Preview your note at the bottom.\n'
        )
    else:
        filepath = os.path.join(pwd, 'kwiki', 'ref', note)
        if os.path.isfile(filepath):
            note = codecs.open(filepath, encoding='utf-8').read()
        else:
            note = 'File not found: {0}'.format(filepath)
    form = PageDownFormExample(csrf_enabled=False)
    text = note
    form.pagedown.data = note
    if form.validate_on_submit():
        text = form.pagedown.data
    return render_template('public/ace.html', form=form, text=text)


@blueprint.route('/note/')
@blueprint.route('/note/<note>/')
def note(note=None):
    if not note:
        note = pwd
        return render_template('public/note.html', note=note)
    filepath = os.path.join(pwd, 'kwiki', 'ref', note)

    if os.path.isfile(filepath):
        note = codecs.open(filepath, encoding='utf-8').read()
    else:
        note = pwd

    return render_template('public/note.html', note=note)


@blueprint.route('/colors/add/', methods=['GET', 'POST'])
def color_add():
    if request.method == 'GET':
        # log.info('GET /color/add/')
        print 'GET /colors/add/'
    elif request.method == 'POST':
        print 'POST /colors/add'
        today = session.query(ColorSet).filter(ColorSet.date == datetime.datetime.today().strftime('%Y-%m-%d')).first()
        if today.id:
            colorset = today
        else:
            colorset = ColorSet()
            colorset.date = datetime.datetime.today()


        data = dicto(request.form)
        data.colors = data.colors[0].split(',')
        colors = session.query(Color).all()
        color_names = [c.name for c in colors]
        for d in data.colors:
            d = d.strip().lower()
            color = Color()
            color.colorset = colorset
            if d not in color_names:
                print 'adding color:', d
                color.name = d
                session.add(color)
                session.commit()
            else:
                old_color = session.query(Color).filter(Color.name == d).first()
                print old_color.id, old_color.name
                if old_color is not None:
                    colorset.colors.append(old_color)
                    # colorset.date = datetime.datetime.today() + datetime.timedelta(days=1)
                    print 'not adding color:', d
                session.add(colorset)
                session.commit()




    form = ColorForm(csrf_enabled=False)
    return render_template('public/color-form.html', text='', form=form)

@blueprint.route('/')
def home():
    return render_template('public/index.html')
