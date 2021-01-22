# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date

class facturas_model(models.Model):
    _name = 'empresa.facturas_model'
    _description = 'empresa.facturas_model'

    name = fields.Char(string="Referencia", required=True)
    fecha = fields.Date(string="Fecha", required=True, default=date.today())
    cliente = fields.Many2one("empresa.clientes_model", string="Cliente")
    productos_id = fields.One2many("empresa.productos_model", "facturas_id" ,string="Productos")
    base = fields.Float(string="Base", compute="_calc_base")
    iva = fields.Selection(string="IVA", default='21', selection=[('21','21'),('15', '15'),('7', '7'),('0', '0')], required=True)
    total = fields.Float(string="Total", compute="_calc_iva")

    @api.depends('productos_id')
    def _calc_base(self):
        suma = 0
        for i in self.productos_id:
            suma += i.pvp
        self.base = suma

    @api.depends('iva', 'base')
    def _calc_iva(self):
        self.total = ((self.base*int(self.iva))/100)+self.base
        
