# -*- coding: utf-8 -*-

from odoo import models, fields, api


class productos_model(models.Model):
    _name = 'empresa.productos_model'
    _description = 'empresa.productos_model'

    name = fields.Char(string="Nombre", required=True)
    descripcion = fields.Html(string="Descripcion", required=True)
    pvp = fields.Float(string="PVP", default=0 , required=True)
    facturas_id = fields.Many2one("empresa.facturas_model", "Facturas")
