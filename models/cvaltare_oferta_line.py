# -*- coding: utf-8 -*-

from odoo import _, models, fields, api
from odoo.exceptions import ValidationError

class CVAltareOfertaLine(models.Model):
    _name = 'cvaltare.oferta_line'
    _description = 'Lineas de las Ofertas de los Curriculumns'
    _rec_name = 'id'

    status = fields.Selection([('accepted', 'Aceptado'), ('refused', 'Rechazado'), ('waiting', 'En espera')], copy=False)
    ofertas_id = fields.Many2one(string="Oferta", comodel_name="cvaltare.oferta", required=True, ondelete='cascade', readonly=True)
    curriculum_id = fields.Many2one(string='Curriculum', comodel_name='cvaltare.curriculum', required=True, ondelete='restrict')
    nombre = fields.Char(related='curriculum_id.nombre', store=False)
    apellidos = fields.Char(related='curriculum_id.apellidos', store=False)
    mail = fields.Char(related='curriculum_id.mail', store=False)
    cargo = fields.Char(related='curriculum_id.cargo', store=False)
    edad = fields.Integer(related='curriculum_id.edad', store=False)
    observaciones =  fields.Text(string="Observaciones")
    mostrar = fields.Char(compute="_mostrar_context", store=False)
    nombre_oferta = fields.Char(compute="_nombre_oferta", store=False)
    # entrevista_id = fields.Many2one(string='Entrevista', comodel_name='cvaltare.entrevista', ondelete='restrict')
    entrevista_ids = fields.One2many(comodel_name="cvaltare.entrevista", inverse_name="linea_id", string="Oferta ent")

    @api.depends('ofertas_id')
    def _mostrar_context(self):
        self.mostrar = self._context.get('mostrar',False)

    @api.depends('ofertas_id.partner_id')
    def _nombre_oferta(self):
        result = []
        for record in self.ofertas_id.partner_id:
            name = ' '.join((record.commercial_partner_id.name, str(record.commercial_partner_id.id)))
        self.nombre_oferta = name
            # result.append((record.id, name))
        # return result

