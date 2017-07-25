# -*- coding: utf-8 -*-

from odoo import fields, models, api


class OdooEtlShellConfig(models.TransientModel):
    _name = 'odoo_etl_shell.config.settings'
    _inherit = 'res.config.settings'
