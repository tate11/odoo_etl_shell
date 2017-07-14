# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.tools.safe_eval import safe_eval


class DataMapping(models.Model):
    _name = 'etlshell.data_mapping'
    _description = 'Data mapping table'

    # Basic info
    mapping_id = fields.Char('Mapping ID')
    from_value = fields.Text('From value')
    to_value = fields.Text('To value')

    _sql_constraints = [
        ('mapping_id_unique', 'unique(mapping_id)', 'The mapping ID must be unique')
    ]
