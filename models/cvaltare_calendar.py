# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class CalendarEvent(models.Model):
    """ Model for Calendar Event """
    _inherit = 'calendar.event'

    @api.model
    def default_get(self, fields):
        if self.env.context.get('default_entrevista_id'):
            self = self.with_context(
                default_res_model='cvaltare.entrevista', #res_model seems to be lost without this
                default_res_model_id=self.env.ref('cvaltare.model_entrevista').id,
                default_res_id=self.env.context['default_entrevista_id']
            )

        defaults = super(CalendarEvent, self).default_get(fields)

        # sync res_model / res_id to opportunity id (aka creating meeting from lead chatter)
        if 'applicant_id' not in defaults:
            res_model = defaults.get('res_model', False) or self.env.context.get('default_res_model')
            res_model_id = defaults.get('res_model_id', False) or self.env.context.get('default_res_model_id')
            if (res_model and res_model == 'hr.applicant') or (res_model_id and self.env['ir.model'].sudo().browse(res_model_id).model == 'hr.applicant'):
                defaults['applicant_id'] = defaults.get('res_id', False) or self.env.context.get('default_res_id', False)

        return defaults

    def _compute_is_highlighted(self):
        super(CalendarEvent, self)._compute_is_highlighted()
        entrevista_id = self.env.context.get('active_id')
        if self.env.context.get('active_model') == 'cvaltare.entrevista' and entrevista_id:
            for event in self:
                if event.entrevista_id.id == entrevista_id:
                    event.is_highlighted = True

    entrevista_id = fields.Many2one('cvaltare.entrevista', string="Curriculum/Oferta", index=True, ondelete='set null')
