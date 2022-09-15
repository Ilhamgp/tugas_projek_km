from odoo import api, fields, models


class kategoriproduk(models.Model):
    _name = 'sport.kategoriproduk'
    _description = 'New Description'


    name = fields.Selection([
        ('bajuolahraga', 'Baju Olahraga'), 
        ('celanaolahraga', 'Celana Olahraga'), 
        ('sepatuolahraga', 'Sepatu Olahraga'),
        ('alatolahraga', 'Alat Olahraga'),
        ('snack', 'Snack')        
    ], string='Nama Kelompok')

    kode_kelompok = fields.Char(string='Kode Kelompok')
 
    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        if (self.name == 'bajuolahraga'):
            self.kode_kelompok = 'bj'
        elif (self.name == 'celanaolahraga'):
            self.kode_kelompok = 'cl'
        elif (self.name == 'sepatuolahraga'):
            self.kode_kelompok = 'sp'
        elif (self.name == 'alatolahraga'):
            self.kode_kelompok = 'alt'
        elif (self.name == 'snack', 'Snack'):
            self.kode_kelompok = 'snk'

    kode_rak = fields.Char(string='Kode Rak')
    produk_ids = fields.One2many(comodel_name='sport.produk',
                                inverse_name='kategoriproduk_id',
                                string='Daftar Produk')
    # jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Item')
    
    # @api.depends('produk_ids')
    # def _compute_jml_item(self):
    #     for rec in self:
    #         a = self.env['sport.produk'].search([('kategoriproduk_id','=', rec.id)]).mapped('name')
    #         b = len(a)
    #         rec.jml_item = b
    #         rec.daftar = a

    daftar = fields.Char(string='Daftar Isi')