# -*- coding: utf-8 -*-
# from odoo import http


# class RoleBasedViews(http.Controller):
#     @http.route('/role_based_views/role_based_views', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/role_based_views/role_based_views/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('role_based_views.listing', {
#             'root': '/role_based_views/role_based_views',
#             'objects': http.request.env['role_based_views.role_based_views'].search([]),
#         })

#     @http.route('/role_based_views/role_based_views/objects/<model("role_based_views.role_based_views"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('role_based_views.object', {
#             'object': obj
#         })

