# -*- coding: utf-8 -*-

from odoo import fields, models, api


class OdooEtlShellConfig(models.TransientModel):
    _name = 'odoo_etl_shell.config.settings'
    _inherit = 'res.config.settings'

    module_name = fields.Char('Module Name', required=True)
    connection_config = fields.Char('Connection config')
    script_path = fields.Char('Script path')

    @api.multi
    def set_connection_config(self):
        connection_config = self[0].connection_config or ''
        self.env['ir.config_parameter'].set_param('odoo_etl_shell.connection_config', connection_config,  groups=['base.group_system'])

    @api.multi
    def set_script_path(self):
        script_path = self[0].script_path or ''
        self.env['ir.config_parameter'].set_param('odoo_etl_shell.script_path', script_path,  groups=['base.group_system'])

    @api.multi
    def get_default_etl_config(self, fields=None):
        get_param = self.env['ir.config_parameter'].sudo().get_param
        connection_config = get_param('odoo_etl_shell.connection_config', default='')
        script_path = get_param('odoo_etl_shell.script_path', default='')
        return {
            'connection_config': connection_config,
            'script_path': script_path,
        }