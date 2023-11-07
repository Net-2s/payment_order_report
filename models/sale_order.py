# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    fiscal_year = fields.Date(string='Fiscal Year', track_visibility='onchange')
    code_operator = fields.Date(string='Code Operator', track_visibility='onchange')
    imputation = fields.Date(string='Imputation', track_visibility='onchange')
