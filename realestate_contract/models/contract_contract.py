# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ContractContract(models.Model):

    _inherit = "contract.contract"

    real_estate_id = fields.Many2one(comodel_name="real.estate", index=True,)
