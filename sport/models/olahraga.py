from odoo import api, fields, models

class olahraga(models.Model):
    _name = 'sport.olahraga'
    _description = 'deskripsi'

    name = fields.Selection([
        ('darat', 'Darat'), 
        ('udara', 'udara'), 
        ('laut', 'Laut'),
    ], string='Jenis Olahraga')
    usia = fields.Char('usia')
    namaolahraga = fields.Char('nama olahraga')
    resikobahaya = fields.Char('resiko bahaya')
    lokasi_id = fields.Many2one('sport.lokasi', string='lokasi')