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
    
    _inherit = ['mail.thread', 'mail.activity.mixin']

    judul = fields.Char(string="Judul Kasus", required=True)
    deskripsi = fields.Text(string="Deskripsi Kasus", required=True) 
    alamatProduk = fields.Char(string="Alamat Produk", required=True)
    status = fields.Selection(selection = [
        ('0', "Aktif"), ('1', 'Tidak Aktif')
    ], required=True)
    namaPelapor = fields.Char(string = "Nama Pelapor", required=True)
    emailPelapor = fields.Char(string="Email Pelapor", required=True)
    nomorPelapor = fields.Char(string="Nomor Pelapor", required=True)
    
    pegawai = fields.Many2many('res.users', String='Penanggung Jawab Kasus')
    
    @api.model
    def create(self, values):
        record = super(Pengaduan, self).create(values)

        channel_name = f"Discussion Channel for {record.judul}"
        channel = self.env['mail.channel'].create({'name': channel_name, 'public': 'private'})
        administrator_partner = self.env.user.sudo().partner_id

        # Add the administrator as a follower to the channel
        channel.message_subscribe(partner_ids=[administrator_partner.id])

        # Add the current user as a follower to the channel
        channel.message_subscribe(partner_ids=[self.env.user.partner_id.id])

        # Post a message to the channel
        message_body = f"Discussion created for {record.judul}"
        channel.message_post(body=message_body)

        return record
    

# TODO : titip simpan, nanti dihapus

# group_kepala_balai_akses_pegawai,Akses Kepala Balai Data Pegawai,model_disepeng_pegawai,group_disepeng_kepala_balai,1,0,0,0

# group_unit_tugas_akses_pegawai,Akses Unit Tugas Data Pegawai,model_disepeng_pegawai,group_disepeng_unit_tugas,0,0,0,0

# group_admin_akses_pegawai,Akses Admin Data Pegawai,model_disepeng_pegawai,group_disepeng_admin,1,1,1,1

# group_helpdesk_akses_pegawai,Akses Helpesk Data Pegawai,model_disepeng_pegawai,group_disepeng_helpdesk,0,0,0,0