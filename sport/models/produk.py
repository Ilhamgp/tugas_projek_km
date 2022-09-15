from odoo import api, fields, models
class produk(models.Model):
    _name = 'sport.produk'
    _description = 'New Description'

    name = fields.Char(string='Nama Produk')
    harga_beli = fields.Integer(string='Harga Modal',required=True)
    harga_jual = fields.Integer(string='Harga Jual',required=True)
    kategoriproduk_id = fields.Many2one(comodel_name='sport.kategoriproduk', 
                                        string='Kategori Produk',
                                        ondelete='cascade')
    supplier_id = fields.Many2many(comodel_name='sport.supplier', string='Supplier')
    stok = fields.Integer(string='Stok')