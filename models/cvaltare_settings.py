from odoo import fields, models, api, _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    html_template = fields.Char(
        string='Template firma', 
        #related='cvaltare.html_template',
        readonly=False,
        config_parameter='cvaltare.html_template')
#        readonly=False)

    @api.onchange('html_template')
    def _onchange_template(self):
        if self.html_template:
            self.update({
                'html_template': self.html_template
            })

#    def set_values(self):
#        res = super(ResConfigSettings, self).set_values()
#        self.env['ir.config_parameter'].sudo().set_param('html_template', self.html_template)
#        return res