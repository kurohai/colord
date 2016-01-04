#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kurohai
# @Date:   2016-01-04 07:17:36
# @Last Modified by:   root
# @Last Modified time: 2016-01-04 07:49:00

import os


appname = 'Color Divination'
appnamed = 'colord'
SECRET_KEY = 'ReallBigPassphraseWithRandomStringenydM2ANhdcoKwdVa0jWvEsbPFuQpMjf'
SESSION_PROTECTION = 'strong'

pwd = os.path.abspath(os.curdir)
dbpath = '{dir}/{app}.db'.format(dir=pwd, app=appnamed)
dburi = 'sqlite:///{db}'.format(db=dbpath)
