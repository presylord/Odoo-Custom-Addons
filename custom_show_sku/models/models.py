# -*- coding: utf-8 -*-
# custom_module/models.py

# custom_module/models.py

# from odoo import models, fields, api
#
# class CustomProductTemplate(models.Model):
#     _inherit = 'product.template'
#
#     def get_combination_info_website(self, combination=False, product=False, **kwargs):
#         combination_info = super(CustomProductTemplate, self).get_combination_info_website(
#             combination=combination, product=product, **kwargs)
#
#         if product and product.product_variant_id:
#             variant_default_code = product.product_variant_id.default_code
#             combination_info['variant_default_code'] = variant_default_code
#
#             # Add your custom field to the response
#         combination_info['custom_field'] = "test"
#
#         return combination_info
