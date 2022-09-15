from odoo import api, fields, models
class member(models.Model):
    _name = 'sport.member'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    nomem = fields.Char('nomem')
    waktu = fields.Char('waktu')
    