# -*- coding: utf-8 -*-
# from odoo import http


# class Thikathani(http.Controller):
#     @http.route('/thikathani/thikathani/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/thikathani/thikathani/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('thikathani.listing', {
#             'root': '/thikathani/thikathani',
#             'objects': http.request.env['thikathani.thikathani'].search([]),
#         })

#     @http.route('/thikathani/thikathani/objects/<model("thikathani.thikathani"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('thikathani.object', {
#             'object': obj
#         })
