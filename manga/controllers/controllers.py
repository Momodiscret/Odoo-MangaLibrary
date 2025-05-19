# -*- coding: utf-8 -*-
# from odoo import http


# class Manga(http.Controller):
#     @http.route('/manga/manga', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manga/manga/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('manga.listing', {
#             'root': '/manga/manga',
#             'objects': http.request.env['manga.manga'].search([]),
#         })

#     @http.route('/manga/manga/objects/<model("manga.manga"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manga.object', {
#             'object': obj
#         })

