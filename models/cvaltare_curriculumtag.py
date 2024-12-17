# -*- coding: utf-8 -*-

from odoo import fields, models


class CurriculumTag(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "cvaltare.curriculumtag"
    _description = "Etiquetas de Curriculum"
    _order = "name"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "!Ya existe esa etiqueta!"),
    ]

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic
    name = fields.Char("Nombre de la etiqueta", required=True)
    color = fields.Integer("Color")
