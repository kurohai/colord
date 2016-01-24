from flask import Blueprint
from flask import render_template, request, url_for
from dicto import dicto
from sqlalchemy import and_
from pprint import pprint
import codecs
import os
from flaskapp import *


blueprint = Blueprint(flasktemplate.appnamed, __name__)



@blueprint.route('/colors/add/', methods=['GET', 'POST'])
def color_add():
    if request.method == 'GET':
        log.info('GET /color/add/')
    elif request.method == 'POST':
        log.info('POST /colors/add')
        today = session.query(ColorSet).filter(ColorSet.date == datetime.datetime.today().strftime('%Y-%m-%d')).first()
        if today:
            if today.id:
                log.info('set found')
                colorset = today
            else:
                log.info('new set created')
                colorset = ColorSet()
                colorset.date = datetime.datetime.today()
        else:
            log.info('new set created')
            today = colorset = ColorSet()

        data = dicto(request.form)

        data.colors = data.colors[0].split(',')
        colors = session.query(Color).all()
        color_names = [c.name for c in colors]
        for d in data.colors:
            d = d.strip().lower()
            color = Color()
            color.colorset = colorset
            if d not in color_names:
                log.info('adding color: {0}'.format(d))
                color.name = d
                session.add(color)
                session.commit()
            else:
                old_color = session.query(Color).filter(Color.name == d).first()
                log.info('old color id: {0}, old color name: {1}'.format(old_color.id, old_color.name))
                # print old_color.id, old_color.name
                if old_color is not None:
                    colorset.colors.append(old_color)
                    # colorset.date = datetime.datetime.today() + datetime.timedelta(days=1)
                    # print 'not adding color:', d
                    log.info('not adding color: {0}'.format(d))

                session.add(colorset)
                session.commit()




    form = ColorForm(csrf_enabled=False)
    return render_template('public/color-form.html', text='', form=form)

@blueprint.route('/')
def home():
    return render_template('public/index.html')
