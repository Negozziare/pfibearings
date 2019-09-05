# -*- coding: utf-8 -*-

from odoo import models,fields,api
  
class Company(models.Model):
    _inherit = 'res.company'

    group_hide_field = fields.Boolean('Show Field')

from odoo import models,fields,api
  
class res_parner(models.Model):
    _inherit = 'res.partner'

    is_show = fields.Boolean('Show Field', compute='_compute_field')

    def _compute_field(self):
        for record in self:
            record.is_show = self.env.user.company_id.group_hide_field
        
class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_show = fields.Boolean('Show Field', compute='_compute_field')

    def _compute_field(self):
        for record in self:
            record.is_show = self.env.user.company_id.group_hide_field
