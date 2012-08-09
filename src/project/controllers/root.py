# encoding: utf-8

import web.core


class RootController(web.core.Controller):
    def index(self):
        return "Hello world!"
