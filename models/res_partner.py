from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = "res.partner"

    fiscal_num = fields.Char(string="NIF", track_visibility='onchange')
    stat_num = fields.Char(string="N° STAT", track_visibility='onchange')
    bank_account = fields.Char(string='Numéro de compte', required=True, track_visibility='onchange')

    @api.onchange('bank_account')
    def update_bank_ids(self):
        for partner in self:
            if partner.bank_account:
                partner.bank_ids = [(0, 0, {
                    'acc_number': partner.bank_account,
                    # Include other relevant fields for the res.partner.bank model
                })]

