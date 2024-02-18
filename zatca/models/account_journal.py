from odoo import models, fields, api


class zatca(models.Model):
    _inherit ='account.journal'

    store_id=fields.Integer(string='Store Id')
    store_code=fields.Char(string='Store Code')
    store_name=fields.Char(string='Store Name')

    _sql_constraints = [
        ('mobile_unique', "unique(store_id)", "Stored ID must be unique sql constrains")]
_sql_constraints = [
        ('mobile_unique', "unique(store_code)", "Stored Name must be unique sql constrains")]

