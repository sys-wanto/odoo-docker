# -*- coding: utf-8 -*-
# from odoo import http


# class OnlineStore(http.Controller):
#     @http.route('/online_store/online_store', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/online_store/online_store/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('online_store.listing', {
#             'root': '/online_store/online_store',
#             'objects': http.request.env['online_store.online_store'].search([]),
#         })

#     @http.route('/online_store/online_store/objects/<model("online_store.online_store"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('online_store.object', {
#             'object': obj
#         })
