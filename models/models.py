from odoo import api, models, fields

class Pegawai(models.Model):
    _name = 'disepeng.pegawai'
    _description = 'Data Pegawai BPOM Makassar'
    
    namaLengkap = fields.Char(string='Nama Lengkap', required=True)
    nomorTelp = fields.Char(string='Nomor Telepon', required=True)
    email = fields.Char(string='Email', required=True)
    peran = fields.Char(string='Peran', required=True)
    isAdmin = fields.Boolean(string='Admin', required=True, default=False)
    
    pengaduan_id = fields.Many2many('disepeng.pengaduan', string="Penanggung Jawab Kasus", required=True)
    

class Pengaduan(models.Model):
    _name = 'disepeng.pengaduan'
    _description = 'Data Kasus'
    
    judul = fields.Char(string="Judul Kasus", required=True)
    deskripsi = fields.Text(string="Deskripsi Kasus", required=True) 
    alamatProduk = fields.Char(string="Alamat Produk", required=True)
    status = fields.Selection(selection = [
        ('0', "Aktif"), ('1', 'Tidak Aktif')
    ])
    namaPelapor = fields.Char(string = "Nama Pelapor", required=True)
    emailPelapor = fields.Char(string="Email Pelapor", required=True)
    nomorPelapor = fields.Char(string="Nomor Pelapor", required=True)
    