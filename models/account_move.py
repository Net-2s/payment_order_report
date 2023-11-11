# -*- coding: utf-8 -*-
from datetime import datetime

from num2words import num2words

from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = "account.move"

    sequence_number = fields.Char(string='Sequence Number', readonly=True, copy=False,
                                  compute='_compute_sequence_number')

    def _compute_sequence_number(self):
        for invoice in self:
            sequence = self.env['ir.sequence'].next_by_code('payment.order.sequence')
            invoice.sequence_number = sequence
            return sequence

    def convert_amount_to_words(self, amount):
        return num2words(amount, lang='fr').title()

    def _compute_current_date(self):
        current_date = datetime.now()
        formatted_date = current_date.date().strftime("%d/%m/%Y")
        return formatted_date
