# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from subprocess import Popen


class IRCronInstance(models.Model):
    _name = 'ir.cron.instance'
    _description = 'Scheduled Action Instance'

    # Basic info
    name = fields.Char('Job Instance ID', required=True)
    step_id = fields.Many2one('etl.step', string='Related Step')
    pid = fields.Integer('Process ID')
    progress = fields.Integer('Progress')
    # Need to check every 1 sec if its running
    run_state = fields.Selection([('start', 'Start'),
                                  ('run', 'Run'),
                                  ('stop',  'Stop'),
                                  ('pause', 'Pause')], string='Run State', default='start')
    cron_id = fields.Many2one('ir.cron', string='Scheduled Action')
    date_start = fields.Datetime('Instance Start', default=lambda self: fields.datetime.now())
    date_end = fields.Datetime('Instance End', help='if not empty, it means that the job is completed')

    @api.model
    def run_next_steps(self):
        """ This method must be instantiated from the xml-rpc
        Using the correct parent step_id

        :return:
        """

        next_steps = self.env['etl.step'].search([('parent_id', '=', self.step_id)])
        for step in next_steps:
            step.date_end = fields.datetime.now()
            if step.script_path:
                p = Popen([step.script_path, step.id], shell=True)
                self.env['ir.cron.instance'].sudo().create({
                    'name': step.name,
                    'step_id': step.id,
                    'pid': p.pid
                })
