# -*- coding: utf-8 -*-

from odoo import _, models, fields, api
from odoo.exceptions import ValidationError

class CVAltareOferta(models.Model):
    _name = 'cvaltare.oferta'
    _description = 'Ofertas de los Curriculumns'
    
    name = fields.Char(string="Descripcion Oferta")
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one("res.partner", string="Cliente", required=True)
    observaciones = fields.Text("Descripción")
    linea_ids = fields.One2many(comodel_name="cvaltare.oferta_line", inverse_name="ofertas_id", string="Oferta")
    mostrar = fields.Char(compute="_mostrar_context", store=False)
    user_id = fields.Many2one("res.users", string="Vendedor", default=lambda self: self.env.user)

    @api.depends('partner_id')
    def _mostrar_context(self):
        self.mostrar = self._context.get('mostrar',False)

    @api.depends('partner_id')
    def name_get(self):
        result = []
        for record in self:
            name = ' '.join((record.partner_id.commercial_partner_id.name, str(record.id)))
            result.append((record.id, name))
        return result
