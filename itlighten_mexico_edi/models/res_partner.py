# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    check_mexican = fields.Boolean(String='Mexican')

    @api.onchange('country_id')
    def onchange_country_id(self):
        if self.country_id and self.country_id.name == 'Mexico':
            self.check_mexican = True
        else:
            self.check_mexican = False





