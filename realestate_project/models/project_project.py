# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProjectProject(models.Model):

    _inherit = "project.project"

    real_estate_id = fields.Many2one(comodel_name="real.estate",)
