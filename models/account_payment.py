from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    manual_usd_rate = fields.Float(
        string='Manual USD Rate',
        digits=(16, 4),
        tracking=True,
        help='Manual USD exchange rate. If set, this rate will be used instead of the system rate.',
    )

    @api.onchange('manual_usd_rate', 'currency_id', 'amount')
    def _onchange_manual_usd_rate(self):
        if self.currency_id and self.manual_usd_rate and self.currency_id.name == 'USD':
            self.force_amount_company_currency = self.amount * self.manual_usd_rate
