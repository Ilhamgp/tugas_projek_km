from odoo import api, fields, models
class lokasi(models.Model):
    _name = 'sport.lokasi'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    harga = fields.Integer('harga')
    lapangan_ids = fields.One2many('sport.olahraga', 'lokasi_id', string='lapangan')
    detail = fields.Char('detail')