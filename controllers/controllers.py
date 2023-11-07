# -*- coding: utf-8 -*-
# from odoo import http


# class PaymentOrderReport(http.Controller):
#     @http.route('/payment_order_report/payment_order_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/payment_order_report/payment_order_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('payment_order_report.listing', {
#             'root': '/payment_order_report/payment_order_report',
#             'objects': http.request.env['payment_order_report.payment_order_report'].search([]),
#         })

#     @http.route('/payment_order_report/payment_order_report/objects/<model("payment_order_report.payment_order_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('payment_order_report.object', {
#             'object': obj
#         })
