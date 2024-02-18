from odoo import models, fields, api


class InheritAccountMove(models.Model):
    _inherit ='account.move'


    #
    # @api.depends('journal_id')
    # def assign_name(self):
    #
    #     for rec in self:
    #         rec.store_name=rec.journal_id.ref




