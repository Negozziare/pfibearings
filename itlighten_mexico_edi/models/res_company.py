# -*- coding: utf-8 -*-

from odoo import models,fields,api
  
class Company(models.Model):
    _inherit = 'res.company'

    mx_fields = fields.Boolean('MX Fields')

        
class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_show = fields.Boolean('Show Field', compute='_compute_field')

    def _compute_field(self):
        for record in self:
            record.is_show = self.env.user.company_id.mx_fields
