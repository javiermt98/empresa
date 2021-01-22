# -*- coding: utf-8 -*-

from odoo import models, fields, api


class clientes_model(models.Model):
    _name = 'empresa.clientes_model'
    _description = 'empresa.clientes_model'


    name = fields.Char(string="Nombre", required=True)
    dni = fields.Char(string="DNI", required=True)
    foto = fields.Binary(string="Foto")
    apellidos = fields.Char(string="Apellidos", required=True)
    telf = fields.Integer(string="Teléfono")
    facturas = fields.One2many("empresa.facturas_model","facturas_id", string="Facturas")
    clientes_id = fields.Many2many("empresa.clientes_model", "Clientes")