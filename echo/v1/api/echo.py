# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas


class Echo(Resource):

    def get(self):
        echo = request.args.get('echo')
        response = {
            'hello': 'world',
            'echo' : echo or ''
        }
        return response, 200, None
