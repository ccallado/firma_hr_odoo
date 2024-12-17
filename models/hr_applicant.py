# -*- coding: utf-8 -*-
# Author: Denis Leemann
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    curriculum_id = fields.Many2one(
        string='Curriculum', comodel_name='cvaltare.curriculum', ondelete='restrict'
        )
    external_id = fields.Char(compute="_external_id", store=False)

    @api.depends('job_id')
    def _external_id(self):
        name = self.job_id.address_id.layout_id.get_external_id()
        exter = ''
        for key, value in name.items():
            exter = value
            break

        if exter == "":
            exter = "cvaltare.report_altare"

        # exter = name[self.job_id.address_id.layaut_id.id]
        self.external_id = exter

    @api.onchange('curriculum_id')
    def copiacurri(self):
        if self.email_from == False and self.curriculum_id.__len__() != 0:
            self.email_from = self.curriculum_id.mail
            self.partner_phone = self.curriculum_id.telefono
            if self.curriculum_id.nombre == False:
                self.partner_name = self.curriculum_id.apellidos
            else:
                partesnombre = (self.curriculum_id.nombre, self.curriculum_id.apellidos)
                self.partner_name = " ".join(partesnombre)
            
            self.name = self.curriculum_id.cargo
            self.salary_expected = self.curriculum_id.rango_ini
            self.salary_proposed = self.curriculum_id.rango_fin
            self.categ_ids = [tag for tag in self.curriculum_id.tag_ids.ids]

    # @api.onchange('email_from')
    # def correo(self):
    #     if self.curriculum_id.__len__() == 0 and self.email_from != False:
    #         # self.curriculum_id.search(['mail', '=', self.email_from])
    #         self.curriculum_id.mail = self.email_from
    #         self.curriculum_id.telefono = self.partner_phone
    #         if self.partner_name == False:
    #             self.curriculum_id.apellidos = self.partner_name
    #
    #        # self.curriculum_id.cargo = self.name
