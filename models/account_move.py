from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.onchange('invoice_lines_ids')
    def _sum_quantity(self, tot_qty=0):

        for rec in self:
            for line in rec.invoice_line_ids:
                # print(line.quantity)
                tot_qty += line.quantity

        self.tot_qty = tot_qty



    x_mrn = fields.Char('MRN')
    tot_qty = fields.Float(compute="_sum_quantity", string="Quantità Totale")
    bank_name = fields.Many2one("res.bank", related="partner_bank_id.bank_id", string="Nome e SWIFT", store=True)

    @api.onchange('invoice_user_id')
    def onchange_ref_purchase(self):
        if self.move_type not in ['out_invoice', 'out_refund']:
            self.ref_purchase_id=self.invoice_user_id.id
    ref_purchase_id =fields.Many2one(
        'res.users',
        string="Referente acquisti",
        default=lambda self: self.env.user
    )

