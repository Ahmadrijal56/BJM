from odoo import models, fields

class Mekanik(models.Model):
    _name = 'workshop_bjm.mekanik'
    _description = 'Data Mekanik Workshop BJM'

    name = fields.Char(string='Nama Mekanik', required=True)
    alamat = fields.Char(string='Alamat')
    no_telepon = fields.Char(string='Nomor Telepon')
    email = fields.Char(string='Email')
    pengalaman = fields.Integer(string='Pengalaman (tahun)')
    catatan = fields.Text(string='Catatan')
