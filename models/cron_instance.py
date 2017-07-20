# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.tools.safe_eval import safe_eval


class IRCronInstance(models.Model):
    _name = 'ir.cron.instance'
    _description = 'Scheduled Action Instance'

    # Basic info
    name = fields.Char('Job Instance ID', required=True)
    pid = fields.Integer('Process ID')
    cron_id = fields.Many2one('ir.cron', string='Scheduled Action')
    date_start = fields.Datetime('Instance Start')
    date_end = fields.Datetime('Instance End', help='if not empty, it means that the job is completed')
