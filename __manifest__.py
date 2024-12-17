{
    'name': 'Ampliación del reclutamiento',
    'version': '1.0',
    'category': 'custom',
    'summary': 'Gestión de curriculums',
    'sequence': '10',
    'license': 'LGPL-3',
    'author': 'Carlos Callado',
    'maintainer': 'Carlos Callado',
    'website': 'localhost:80',
    "depends": ['base', 'web', 'sale', 'mail', 'calendar', 'hr_recruitment'],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'views/cvaltare_curriculum_views.xml',
        'views/cvaltare_curriculumtag_views.xml',
        'views/cvaltare_oferta_views.xml',
        'views/cvaltare_oferta_line_views.xml',
        'views/cvaltare_entrevista_views.xml',
        'views/cvaltare_menus.xml',
        'views/applicant.xml',     
        'views/res_partner_form.xml',
        # 'reports/add_custom_footer_in_qweb_report.xml',
        # 'reports/add_custom_header_in_qweb_report.xml',
        'reports/report_templates.xml',
        # 'reports/cvaltare_report_cu.xml',
        # 'reports/cvaltare_report_views_cu.xml',
        'reports/cvaltare_report.xml',
        'reports/cvaltare_report_views.xml',
        'views/hr_employee.xml',
        'views/cvaltare_settings.xml',
    ],
    'installable': True,
    'application': True,
    'auto install': False,
}
