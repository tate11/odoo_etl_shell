from odoo import fields, models, api
from subprocess import Popen


class JobSteps(models.Model):
    _name = 'etl.step'

    name = fields.Char('Step Name')
    default_timeout = fields.Integer('Default Timeout(s)', help='Default timeout in seconds')
    parent_id = fields.Many2one('etl.step', string='Parent Step')
    # will not be used if parent_id=False because on startup we use
    # config param: odoo_etl_shell.script_path
    script_path = fields.Char('Script Path')

    @api.model
    def run_steps(self):
        get_param = self.env['ir.config_parameter'].sudo().get_param
        startup_job = self.env['etl.job'].search([('parent_id', '=', False)])
        # If parent_id=False then we must run the ir.config_parameter
        if startup_job:
            cron_job = self.env['ir.cron'].sudo().search([('start_job_id', '=', startup_job.id)])
            script_path = get_param('odoo_etl_shell.script_path', default=False)
            if script_path:
                p = Popen([script_path], shell=True)
                self.env['ir.cron.instance'].sudo().create({
                    'name': startup_job.name,
                    'cron_id': cron_job.id,
                    'pid': p.pid
                })


class IRCron(models.Model):
    _inherit = 'ir.cron'

    instance_ids = fields.One2many('ir.cron.instance', 'cron_id', string='Job Instances')
    start_job_id = fields.Many2one('etl.step', string='Startup Step')
