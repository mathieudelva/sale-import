#  Copyright (c) Akretion 2020
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
from odoo.addons.datamodel import fields
from odoo.addons.datamodel.datamodels.base import BaseDatamodel


class SaleOrderAmountDatamodel(BaseDatamodel):
    _name = "sale.order.amount"

    amount_tax = fields.Decimal(required=True)
    amount_untaxed = fields.Decimal(required=True)
    amount_total = fields.Decimal(required=True)
