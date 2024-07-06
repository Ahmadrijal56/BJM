from odoo import models, fields, api

class DataKonsumen(models.Model):
    _name = 'workshop_bjm.data_konsumen'
    _description = 'Data Konsumen Workshop BJM'

    name = fields.Char(string='Name')
    alamat = fields.Char(string='Alamat')
    no_polisi = fields.Char(string='No Polisi', required=True)
    no_telepon = fields.Char(string='No Telepon')
    no_fax = fields.Char(string='No Fax')
    no_km = fields.Integer(string='KM')
    tanggal_service = fields.Date(string='Tanggal Service', required=True)
    no_faktur = fields.Char(string='No Faktur', required=True)
    kode_dokumen = fields.Char(string='Kode Dokumen', readonly=True, copy=False, default='New')
    month = fields.Integer(string='Bulan')
    year = fields.Integer(string='Tahun')
    data_konsumen_line_ids = fields.One2many('workshop_bjm.data_konsumen_line', 'data_konsumen_id', string='Data Konsumen Line')

    merk_mobil_id = fields.Many2one('workshop_bjm.car_brand', string='Merk Mobil', required=True)
    varian_mobil_id = fields.Many2one('workshop_bjm.car_type', string='Varian Mobil', domain="[('brand_id', '=', merk_mobil_id)]", required=True)

    # Computed fields for search
    search_nama_barang = fields.Char(string='Search Nama Barang', compute='_compute_search_fields', store=True)
    search_mekanik = fields.Char(string='Search Mekanik', compute='_compute_search_fields', store=True)
    search_keterangan = fields.Char(string='Search Keterangan', compute='_compute_search_fields', store=True)

    @api.depends('data_konsumen_line_ids.nama_barang', 'data_konsumen_line_ids.mekanik', 'data_konsumen_line_ids.keterangan')
    def _compute_search_fields(self):
        for record in self:
            record.search_nama_barang = ' '.join([line.nama_barang or '' for line in record.data_konsumen_line_ids])
            record.search_mekanik = ' '.join([mekanik.name or '' for line in record.data_konsumen_line_ids for mekanik in line.mekanik])
            record.search_keterangan = ' '.join([line.keterangan or '' for line in record.data_konsumen_line_ids])


    @api.model
    def create(self, vals):
        if vals.get('kode_dokumen', 'New') == 'New':
            sequence_code = 'workshop_bjm.data_konsumen'
            current_date = fields.Date.context_today(self)
            vals['month'] = current_date.month
            vals['year'] = current_date.year
            new_sequence = self.env['ir.sequence'].next_by_code(sequence_code) or 'New'
            formatted_code = f'BJM/{current_date.month}/{current_date.year}/{new_sequence}'
            vals['kode_dokumen'] = formatted_code
        result = super(DataKonsumen, self).create(vals)
        return result

    def copy(self, default=None):
        if default is None:
            default = {}
        default.update({
            'tanggal_service': False,
            'no_faktur': False,
        })
        return super(DataKonsumen, self).copy(default)



class DataKonsumenLine(models.Model):
    _name = 'workshop_bjm.data_konsumen_line'
    _description = 'Detail Layanan/Barang Data Konsumen'

    data_konsumen_id = fields.Many2one('workshop_bjm.data_konsumen', string='Data Konsumen')
    nama_barang = fields.Char(string='Nama Barang')
    mekanik = fields.Many2many('workshop_bjm.mekanik', string='Mekanik')
    keterangan = fields.Text(string='Keterangan')

