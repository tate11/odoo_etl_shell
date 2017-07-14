from odoo import fields, models

class script_scheduler(models.Model):
    _name = 'odooetlshell.script_scheduler'
    _inherits = 'ir.cron'

    script_config = fields.Char('Configuration')
    script_schedule_description = fields.Char('Description')
    last_modified = fields.Char('Last updated')
