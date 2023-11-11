# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    fiscal_year = fields.Char(string='Année fiscale', track_visibility='onchange')
    code_operator = fields.Char(string='Code Operateur', track_visibility='onchange')
    imputation = fields.Char(string='Imputation', track_visibility='onchange')
    payment_method = fields.Selection([
        ("cash","Espèce"),
        ("bank_transfer","virement "),
        ("check","Chèque"),],
        string='Methode de paiement',
        default='cash', track_visibility='onchange')
