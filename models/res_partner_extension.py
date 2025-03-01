from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    campo_para_el_rol_1 = fields.Char(string="Campo para el Rol 1")
    campo_para_el_rol_2 = fields.Char(string="Campo para el Rol 2")
