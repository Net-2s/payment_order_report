# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    fiscal_year = fields.Char(string='Fiscal Year', track_visibility='onchange')
    code_operator = fields.Char(string='Code Operator', track_visibility='onchange')
    imputation = fields.Char(string='Imputation', track_visibility='onchange')
    payment_method = fields.Selection([
        ("cash","Espèce"),
        ("bank_transfer","virement "),
        ("check","Chèque"),],
        string='Payment Method',
        default='cash', track_visibility='onchange')
