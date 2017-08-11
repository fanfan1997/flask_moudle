#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from . import db


class TestModel(db.Document):
    meta = {
        'collection': 'mytest',
    }
    name = db.StringField()
    created = db.DateTimeField(default=datetime.datetime.now())
