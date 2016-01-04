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


@blueprint.route('/')
def home():
    return render_template('public/index.html')
