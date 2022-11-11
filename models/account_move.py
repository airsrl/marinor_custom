from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = 'account.move'


    agenti = fields.Char(compute="_compute_agents_name", string="agenti")

    @api.depends("invoice_line_ids")
    def _compute_agents_name(self):
        for record in self:
                record.agenti = record.partner_agent_ids.display_name