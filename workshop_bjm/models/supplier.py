from odoo import models, fields, api

class Supplier(models.Model):
    _name = 'workshop_bjm.supplier'
    _description = 'Supplier Data for Workshop BJM'

    name = fields.Char(string='Nama Supplier', required=True)
    alamat = fields.Text(string='Alamat')
    produk = fields.Many2many('workshop_bjm.kategori_produk', string='Produk')
    no_telepon = fields.Char(string='Nomor Telepon')
    email = fields.Char(string='Email')
    catatan = fields.Text(string='Catatan')
