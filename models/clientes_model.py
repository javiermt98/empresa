# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class clientes_model(models.Model):
    _name = 'empresa.clientes_model'
    _description = 'empresa.clientes_model'


    name = fields.Char(string="Nombre", required=True)
    dni = fields.Char(string="DNI", required=True)
    foto = fields.Binary(string="Foto", required="False")
    apellidos = fields.Char(string="Apellidos", required=True)
    telf = fields.Integer(string="Teléfono")
    facturas = fields.One2many("empresa.facturas_model","cliente", string="Facturas")

    @api.constrains("dni")
    def _comprobarDNI(self):
        if len(self.dni)!=9:
            raise ValidationError("El DNI debe tener 9 caracteres")
        else:
            try:
                n=int(self.dni[:-1])
            except ValueError:
                raise ValidationError("Los primeros 8 dígitos deben ser números")

            palabra='TRWAGMYFPDXBNJZSQVHLCKE'

            if self.dni[-1].upper() == palabra[n%23]:
                return True
            else:
                
                raise ValidationError("La letra no coincide con el DNI")
