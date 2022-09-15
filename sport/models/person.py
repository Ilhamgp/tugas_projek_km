from odoo import api, fields, models


class person(models.Model):
    _name = 'sport.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Datetime(string='Tanggal Lahir')


class kasir(models.Model):
    _name = 'sport.kasir'
    _inherit = 'sport.person'
    _description = 'New Description'

    id_kasir = fields.Char(string='ID Kasir')


class admin(models.Model):
    _name = 'sport.admin'
    _inherit = 'sport.person'
    _description = 'New Description'

    id_adm = fields.Char(string='ID Admin')