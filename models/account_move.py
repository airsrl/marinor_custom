from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    # agenti = fields.Char(related='partner_agent_ids.display_name', string="agenti")
    # price_lst = fields.Float(related="", string="Prezzo listino")
    # calc_disc = fields.Float(compute="", string="Sconto Calcolato")

    # @api.depends("invoice_line_ids")
    # def _compute_agents_name(self):
    #     for record in self:
    #             record.agenti = record.partner_agent_ids.display_name

    