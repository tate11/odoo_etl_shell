# -*- coding: utf-8 -*-

from odoo import fields, models, api


class EtlShell(models.TransientModel):
    _name = 'etlshell.config.settings'
    _inherit = 'res.config.settings'

    connection_config = fields.Char('Connection config')
    script_path = fields.Char('Job script path')

    @api.multi
    def set_connection_config(self):
        connection_config = self[0].connection_config or ''
        self.env['ir.config_parameter'].set_param(self._name, connection_config,  groups=['base.group_system'])

    @api.multi
    def set_script_path(self):
        script_path = self[0].connection_config or ''
        self.env['ir.config_parameter'].set_param(self._name, script_path,  groups=['base.group_system'])

    @api.multi
    def get_default_etl_config(self, fields=None):
        get_param = self.env['ir.config_parameter'].sudo().get_param
        connection_config = get_param(self._name + '.connection_config', default='')
        script_path = get_param(self._name + '.script_path', default='')
        return {
            'connection_config': connection_config,
            'script_path': script_path,
        }