# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class RealEstate(models.Model):

    _inherit = "real.estate"

    project_ids = fields.One2many(
        comodel_name="project.project", inverse_name="real_estate_id",
    )
