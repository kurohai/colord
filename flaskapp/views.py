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

@blueprint.route('/colors/add/', methods=['GET', 'POST'])
def color_add():
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

        tmp = list()
        for c in data.colors:
            n = c.split('\r\n')
            for nerp in n:
                tmp.append(nerp)
        data.colors = tmp


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
            pprint(c)
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





@blueprint.route('/')
def home():
    return render_template('public/index.html')
