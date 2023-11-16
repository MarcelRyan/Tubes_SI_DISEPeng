from odoo import models, fields

class Pelapor(models.Model):
    _name = 'disepeng.pelapor'
    _description = 'Data Pelapor Kasus'

    namaLengkap = fields.Char(string='Nama Lengkap', required=True)
    alamat = fields.Text(string='Alamat', required=True)
    nomorTelp = fields.Char(string='Nomor Telepon', required=True)
    email = fields.Char(string='Email', required=True)
    gender = fields.Selection(selection = [
        ('0', "Laki-laki"), ("1", "Perempuan")
    ])

class Pengaduan(models.Model):
    _name = 'disepeng.pengaduan'
    _description = 'Data Kasus'
    
    judul = fields.Char(string="Judul Kasus", required=True)
    deskripsi = fields.Text(string="Deskripsi Kasus", required=True) 
    alamatProduk = fields.Char(string="Alamat Produk", required=True)
    status = fields.Selection(selection = [
        ('0', "Aktif"), ('1', 'Tidak Aktif')
    ])
    type = fields.Many2one('disepeng.pelapor', string="Pelapor")

class Pegawai(models.Model):
    _name = 'disepeng.pegawai'
    _description = 'Data Pegawai BPOM Makassar'
    
    namaLengkap = fields.Char(string='Nama Lengkap', required=True)
    nomorTelp = fields.Char(string='Nomor Telepon', required=True)
    email = fields.Char(string='Email', required=True)
    peran = fields.Char(string='Peran', required=True)
    isAdmin = fields.Boolean(string='Admin', required=True, default=False)
    
    pengaduan_id = fields.Many2many('disepeng.pengaduan', string="Penanggung Jawab Kasus", required=True)
    
class Diskusi(models.Model):
    _name = 'disepeng.diskusi'
    _description = 'Data Diskusi Kasus Pengaduan Terkait'
    
    judul = fields.Char(string="Judul Forum", required=True)
    
    pengaduan_id = fields.One2one('disepeng.pengaduan', string="Kasus", required=True)

class Percakapan(models.Model):
    _name = 'disepeng.percakapan'
    _description = 'Data percakapan pada forum diskusi'
    
    pesan = fields.Text(string="Pesan", required=True)
    waktu = fields.Datetime(string="Waktu Pengiriman", required=True)    

    diskusi_id = fields.One2many(string="Diskusi Terkait", required=True)
    pegawai_id = fields.One2many(string="Pengirim pesan", required=True)