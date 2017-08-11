#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import jsonify
from flask_restful import Resource
from app.models import *
from .. import cache
from app import utils
logger = utils.get_logger()


class index(Resource):
    def get(self):
        return 'Welcome to use car_ins_search!!!'


class test(Resource):
    def get(self):
        a = TestModel.objects(name='aaa').count()
        if not a:
            a = TestModel(name='aaa')
            a.save()
        test = TestModel.objects(name='aaa').first()
        cache.set('mykey', 'abc', timeout=10)
        b = cache.get('mykey')
        logger.info({'a': 1, 'b': b})
        return jsonify({'name': test.name, 'created': test.created})
