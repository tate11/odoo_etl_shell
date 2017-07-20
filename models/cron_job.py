from odoo import fields, models, api
from subprocess import Popen


class JobSteps(models.Model):
    """ Defines sequential script steps for ETL routines
    The target script will be in charge of running the
    next steps using a xml-rpc call on the step object
    """

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
        start_step = self.env['etl.step'].search([('parent_id', '=', False)])
        # If parent_id=False then we must run the ir.config_parameter
        if start_step:
            cron_job = self.env['ir.cron'].sudo().search([('start_job_id', '=', start_step.id)])
            script_path = get_param('odoo_etl_shell.script_path', default=False)
            if script_path:
                # First argument of the script ($1) will be the step_id
                p = Popen([script_path, start_step.id], shell=True)
                self.env['ir.cron.instance'].sudo().create({
                    'name': start_step.name,
                    'step_id': start_step.id,
                    'cron_id': cron_job.id,
                    'pid': p.pid
                })


class IRCron(models.Model):
    _inherit = 'ir.cron'

    instance_ids = fields.One2many('ir.cron.instance', 'cron_id', string='Job Instances')
    start_job_id = fields.Many2one('etl.step', string='Startup Step')
