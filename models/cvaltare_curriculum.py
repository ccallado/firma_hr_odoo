# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class CVAltareCurriculum(models.Model):
    _name = 'cvaltare.curriculum'
    _description = 'Curriculums'
    _order = "mail"
    _rec_name= "mail"
    _inherit = "mail.thread"

    nombre = fields.Char("Nombre", tracking=True)
    apellidos = fields.Char("Apellidos", required=True, tracking=True)
    cargo = fields.Char("Cargo que tuvo", tracking=True)
    calle = fields.Char("Dirección", tracking=True)
    codpos = fields.Char("Código postal", tracking=True)
    poblacion = fields.Char("Población", tracking=True)
    provincia = fields.Char("Provincia", tracking=True)
    edad = fields.Integer("Edad", tracking=True)
    fchnaci = fields.Date("Fecha de nacimiento", tracking=True)
    telefono = fields.Char("Teléfono", tracking=True)
    mail = fields.Char("Email", required=True, tracking=True)
    experiencia = fields.Html("Experiencia")
    estudios = fields.Html("Estudios")
    conocimientos = fields.Html("Conocimientos")
    idiomas = fields.Html("Idiomas")
    tag_ids = fields.Many2many('hr.applicant.category', string="Etiquetas", tracking=True)
    codigo = fields.Integer("Código", tracking=True)
    rango_ini = fields.Float("Salario esperado", tracking=True)
    rango_fin = fields.Float("Salario propuesto", tracking=True)
    active = fields.Boolean('Active', default=True, tracking=True)
    oferta_ids = fields.One2many("cvaltare.oferta_line", inverse_name="curriculum_id", string="Ofertas", required=True, tracking=True)
    applicant_ids = fields.One2many("hr.applicant", inverse_name="curriculum_id", string="Postulaciones")
    mostrar = fields.Char(compute="_mostrar_context", store=False)
    used = fields.Boolean(compute='_compute_used', search='_search_used')
    company_id = fields.Many2one('res.company', required=True, readonly=True, default=lambda self: self.env.company)
    _sql_constraints = [
        ('unique_mail', 'unique (mail)', '!Ya existe el EMail!')
    ]

    @api.depends('rango_ini')
    def _mostrar_context(self):
        self.mostrar = self._context.get('mostrar',False)

    def _search_used(self, operator, value):
        if operator not in ['=', '!='] or not isinstance(value, bool):
            raise UserError(_('Operation not supported'))
        if operator != '=':
            value = not value
        # self._cr.execute("""
        #     SELECT id FROM cvaltare_curriculum curriculum
        #     WHERE EXISTS (SELECT * FROM cvaltare_oferta_line cvol WHERE cvol.curriculum_id = curriculum.id AND (cvol.status <> 'refused' OR cvol.status IS NULL) LIMIT 1)
        # """)
        self._cr.execute("""
            SELECT id FROM cvaltare_curriculum curriculum
            WHERE EXISTS (SELECT * FROM hr_applicant cvol WHERE cvol.curriculum_id = curriculum.id AND (cvol.active = 'True') LIMIT 1)
        """)
        return [('id', 'in' if value else 'not in', [r[0] for r in self._cr.fetchall()])]

    def _compute_used(self):
        ids = set(self._search_used('=', True)[0][2])
        for record in self:
            record.used = record.id in ids


