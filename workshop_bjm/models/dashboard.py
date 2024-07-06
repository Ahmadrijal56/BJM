from odoo import models, fields, api
from datetime import datetime, timedelta

class Dashboard(models.Model):
    _name = 'workshop_bjm.dashboard'
    _description = 'Workshop BJM Dashboard'

    name = fields.Char(string='Name', default='Dashboard')
    invoice_month_count = fields.Integer(string='Invoices This Month', compute='_compute_invoice_counts')
    invoice_week_count = fields.Integer(string='Invoices This Week', compute='_compute_invoice_counts')
    customer_count = fields.Integer(string='Customers', compute='_compute_customer_count')
    mechanic_count = fields.Integer(string='Mechanics', compute='_compute_mechanic_count')
    supplier_count = fields.Integer(string='Suppliers', compute='_compute_supplier_count')

    @api.depends('name')
    def _compute_invoice_counts(self):
        for record in self:
            today = fields.Date.today()
            start_of_month = today.replace(day=1)
            start_of_week = today - timedelta(days=today.weekday())
            record.invoice_month_count = self.env['account.move'].search_count([
                ('invoice_date', '>=', start_of_month),
                ('state', '=', 'posted')
            ])
            record.invoice_week_count = self.env['account.move'].search_count([
                ('invoice_date', '>=', start_of_week),
                ('state', '=', 'posted')
            ])

    @api.depends('name')
    def _compute_customer_count(self):
        for record in self:
            record.customer_count = self.env['res.partner'].search_count([('customer_rank', '>', 0)])

    @api.depends('name')
    def _compute_mechanic_count(self):
        for record in self:
            record.mechanic_count = self.env['workshop_bjm.mekanik'].search_count([])

    @api.depends('name')
    def _compute_supplier_count(self):
        for record in self:
            record.supplier_count = self.env['workshop_bjm.supplier'].search_count([])

    def action_open_invoices(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoices',
            'res_model': 'account.move',
            'view_mode': 'tree,form',
            'domain': [('state', '=', 'posted')],
        }

    def action_open_customers(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Customers',
            'res_model': 'res.partner',
            'view_mode': 'tree,form',
            'domain': [('customer_rank', '>', 0)],
        }

    def action_open_mechanics(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Mechanics',
            'res_model': 'workshop_bjm.mekanik',
            'view_mode': 'tree,form',
        }

    def action_open_suppliers(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Suppliers',
            'res_model': 'workshop_bjm.supplier',
            'view_mode': 'tree,form',
        }
