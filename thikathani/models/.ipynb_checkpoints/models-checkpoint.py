# -*- coding: utf-8 -*-

from odoo import models, fields, api


class thikathani(models.Model):
    _inherit = "product.template"
    region = fields.Char("Region del Peru")
#     _name = 'thikathani.thikathani'
#     _description = 'thikathani.thikathani'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
