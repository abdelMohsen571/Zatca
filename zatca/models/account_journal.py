from odoo import models, fields, api


class zatca(models.Model):
    _inherit ='account.journal'

    ref=fields.Char(string='References')
