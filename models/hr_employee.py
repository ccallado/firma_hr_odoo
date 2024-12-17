# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import imgkit, base64
# import base64

class HrEmployeeFirma(models.Model):
    _inherit = "hr.employee"
    _name = "hr.employee"
    _description = "Firma Mail Empleados"

    firma_html  = fields.Html(string='HTML')
    firma_image = fields.Binary(string='Imagen')

    def write(self, vals):
        try:
            nombre = vals['name']
        except:
            if self.name != False:
                nombre = self.name
            else:
                nombre = ''

        try:
            cargo = vals['job_title']
        except:
            if self.job_title != False:
                cargo = self.job_title
            else:
                cargo = ''

        try:
            telef = vals['mobile_phone']
        except:
            if self.mobile_phone != False:
                telef = self.mobile_phone
            else:
                telef = ''
            

        try:
            mail = vals['work_email']
        except:
            if self.work_email != False:
                mail = self.work_email
            else:
                mail = ''

        (vals['firma_html'], vals['firma_image']) = self.crear_firma(nombre, cargo, telef, mail)
        res = super().write(vals)
        return res

    @api.model
    def create(self, values):
        """Override default Odoo create function and extend."""
        (values['firma_html'], values['firma_image']) = self.crear_firma(values['name'], values['job_title'], values['mobile_phone'], values['work_email'])
        res = super(HrEmployeeFirma, self).create(values)
        return res

    def crear_firma(self, nombre, cargo, telef, mail):
        firma_html = self.env['ir.config_parameter'].sudo().get_param('cvaltare.html_template')
        firma_html = firma_html.replace("<<NOMBRE>>", nombre)
        firma_html = firma_html.replace("<<CARGO>>", cargo)
        firma_html = firma_html.replace("<<TELEF>>", telef)
        firma_html = firma_html.replace("<<MAIL>>", mail)
        imgkit.from_string(firma_html, 'imagen.jpg')
        with open('imagen.jpg', 'rb') as f:
          firma_image = base64.b64encode(f.read())
        return (firma_html, firma_image)
    
    def action_crear_firma(self):
        f = ''
        vals = {}
        for employee in self.browse(self.env.context['active_ids']):
            (f, employee.firma_image) = self.crear_firma(employee.name, employee.job_title, employee.mobile_phone, employee.work_email)
            vals['firma_html'] = f
            vals['firma_image'] = employee.firma_image
            employee.write(vals)
