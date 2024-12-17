# -*- coding: utf-8 -*-

from odoo import fields, models


class ResPartners(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _inherit = "res.partner"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Relational
    # This domain gives the opportunity to mention the evaluated and non-evaluated domains
    layout_id = fields.Many2one('ir.ui.view', 'Document Template')
