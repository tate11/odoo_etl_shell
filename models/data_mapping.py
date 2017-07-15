# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.tools.safe_eval import safe_eval


class DataMapping(models.Model):
    _name = 'odoo_etl_shell.data_mapping'
    _description = 'Data mapping table'

    # Basic info
    module_name = fields.Char('Module Name', required=True)
    etl_context = fields.Char('Mapping Context')
    from_value = fields.Text('From value')
    to_value = fields.Text('To value')
