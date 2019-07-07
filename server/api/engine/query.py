# -*- coding: utf-8 -*-
# vim:tabstop=4:shiftwidth=4:expandtab

from datetime import (
    datetime,
)

class Response(object):
    def __init__(self):
        self.start_dt = datetime.now()
        self.req = None
        self.res = None
    
    def __call__(self, req, res):
        self.req = req
        self.res = res

        result = self.results()
        meta = self.meta()

        return {
            'meta': meta,
            'results': result,
        }

    def meta(self):
        return {
            'elapsed_time': (datetime.now() - self.start_dt).total_seconds() * (10 ** 6),
            'request_params': self.req
        }
    
    def results(self):
        return {
            'label': self.res,
        }
        

