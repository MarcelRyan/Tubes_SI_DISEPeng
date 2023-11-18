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
    percakapan_ids = fields.One2many('disepeng.percakapan', 'pegawai_id', string="Pengirim Pesan")
    
class Diskusi(models.Model):
    _name = 'disepeng.diskusi'
    _description = 'Data Diskusi Kasus Pengaduan Terkait'
    
    judul = fields.Char(string="Judul Forum", required=True)
    
    pengaduan_id = fields.Many2one('disepeng.pengaduan', string="Pengaduan ID", required=True, ondelete='cascade', unique=True, auto_join=True)
    percakapan_ids = fields.One2many('disepeng.percakapan', 'diskusi_id', string="Percakapan Terkait")

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
    
    diskusi_ids = fields.One2many('disepeng.diskusi', 'pengaduan_id', string="Diskusi Terkait")

class Percakapan(models.Model):
    _name = 'disepeng.percakapan'
    _description = 'Data percakapan pada forum diskusi'
    
    pesan = fields.Text(string="Pesan", required=True)
    waktu = fields.Datetime(string="Waktu Pengiriman", required=True)    

    diskusi_id = fields.Many2one('disepeng.diskusi', string="Diskusi Terkait", required=True, ondelete='cascade')
    pegawai_id = fields.Many2one('disepeng.pegawai', string="Pengirim pesan", required=True)