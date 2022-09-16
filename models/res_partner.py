from odoo import fields, models


class res_partner_marinor(models.Model):
    _inherit = 'res.partner'

    is_cliente = fields.Boolean(
        string="Cliente",
        default=True
    )
    is_fornitore = fields.Boolean(
        string="Fornitore"
    )
    totale = fields.Float(
        compute="_get_totale"
    )

    def _get_totale(self):
        self.totale = 15 * 21