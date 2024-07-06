from odoo import models, fields

class ProductCategory(models.Model):
    _name = 'workshop_bjm.kategori_produk'
    _description = 'Product Category for Workshop BJM'

    name = fields.Char(string='Kategori Produk', required=True)
    description = fields.Text(string='Keterangan')