from odoo import models, fields, api


class InheritAccountMove(models.Model):
    _inherit ='account.move'

    store_id=fields.Integer(string='Store ID')
    store_code=fields.Char(string='Store Code')
    store_name=fields.Char(store='Store Name')

    @api.depends('journal_id')
    def assign_name(self):

        for rec in self:
            rec.store_name=rec.journal_id.ref




