#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask_mongoengine import MongoEngine
from config import config
from flask_restful import Api
from flask_cache import Cache
from flask_mail import Mail

db = MongoEngine()
mail = Mail()
cache = None


def create_app(config_name):
    global cache
    app = Flask(__name__,
                template_folder=config[config_name].TEMPLATE_PATH,
                static_folder=config[config_name].STATIC_PATH)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    cache = Cache(app, config=config[config_name].REDIS_SETTINGS)
    db.init_app(app)
    mail.init_app(app)

    # from app.urls import api as api_blueprint
    # app.register_blueprint(api_blueprint, url_prefix='/api')

    return app

app = create_app(os.getenv('config') or 'default')
api = Api(app)
