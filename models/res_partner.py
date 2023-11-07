from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = "res.partner"

    fiscal_num = fields.Char(string="NIF", track_visibility='onchange')
    stat_num = fields.Char(string="N° STAT", track_visibility='onchange')
    bank_account = fields.Integer(string='Bank account', required=True, track_visibility='onchange')
