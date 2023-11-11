# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import api, fields, models


class PaymentOrderReport(models.AbstractModel):
    _name = 'report.payment.order.report'
    _description = 'Payment Order Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['account.move'].browse(docids)
        current_date = datetime.now()
        return {
            'doc_ids': docs.ids,
            'doc_model': 'account.move',
            'docs': docs,
            'current_date': current_date,
        }
