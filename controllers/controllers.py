# -*- coding: utf-8 -*-
from openerp import http

# class SparkitCmtysByCountryMenu(http.Controller):
#     @http.route('/sparkit_cmtys_by_country_menu/sparkit_cmtys_by_country_menu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sparkit_cmtys_by_country_menu/sparkit_cmtys_by_country_menu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sparkit_cmtys_by_country_menu.listing', {
#             'root': '/sparkit_cmtys_by_country_menu/sparkit_cmtys_by_country_menu',
#             'objects': http.request.env['sparkit_cmtys_by_country_menu.sparkit_cmtys_by_country_menu'].search([]),
#         })

#     @http.route('/sparkit_cmtys_by_country_menu/sparkit_cmtys_by_country_menu/objects/<model("sparkit_cmtys_by_country_menu.sparkit_cmtys_by_country_menu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sparkit_cmtys_by_country_menu.object', {
#             'object': obj
#         })