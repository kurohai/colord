from flask import Blueprint
from flask import render_template, request, url_for
from dicto import dicto
from sqlalchemy import and_
from pprint import pprint
import codecs
import os
from flaskapp import *
from dateme import parse_date

blueprint = Blueprint(flasktemplate.appnamed, __name__)

@blueprint.route('/colors/add2/', methods=['GET', 'POST'])
def color_add2():
    if request.method == 'GET':
        log.info('GET /color/add/')
    elif request.method == 'POST':
        log.info('POST /colors/add')

        data = dicto(request.form)
        data.colors = data.colors[0].split(',')

        # need to do some date formatting here
        # convert input date to iso8601
        input_date = parse_date(data.date[0])
        parsed_date = input_date.strftime('%Y-%m-%d')
        log.info('parsed date: {0}'.format(parsed_date))
        day = session.query(ColorSet).filter(ColorSet.date == parsed_date).first()

        # get the correct colorset
        log.info('setting colorset...')

        # day not yet entered
        if day is None:
            log.info('new colorset')
            colorset = ColorSet()
            colorset.date = input_date

        # day previously entered
        else:
            log.info('found colorset')
            colorset = day

        # add colors to colorset
        for c in data.colors:
            c = c.strip()
            log.info(c)
            color = Color()
            color.name = c

            old_colors = [i.name for i in colorset.colors]
            log.debug('old colors {0}'.format(old_colors))

            if c != '':

                # check if color already added
                if c not in old_colors:
                    log.info('adding color: {0}'.format(c))
                    colorset.colors.append(color)
                else:
                    log.warn('color {0} already entered'.format(c))

        # commit changes to db
        log.debug(colorset.date)
        session.add(colorset)
        session.commit()

    form = ColorForm(csrf_enabled=False)
    return render_template('public/color-form.html', text='', form=form)



@blueprint.route('/colors/add-old/', methods=['GET', 'POST'])
def color_add_old():
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


@blueprint.route('/colors/add/', methods=['GET', 'POST'])
def color_add():
    form = ColorForm(csrf_enabled=False)
    if request.method == 'GET':
        log.info('GET /color/add/')
    elif request.method == 'POST':
        log.info('POST /colors/add')
    return render_template('public/color-form.html', text='', form=form)










@blueprint.route('/')
def home():
    return render_template('public/index.html')
