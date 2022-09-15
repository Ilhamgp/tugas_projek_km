from odoo import api, fields, models


class supplier(models.Model):
    _name = 'sport.supplier'
    _description = 'New Description'

    name = fields.Char(string='Nama Perusahaan')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telepon')
    produk_id = fields.Many2many(comodel_name='sport.produk', string='Produk')