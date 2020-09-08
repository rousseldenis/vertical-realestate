# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, fields, models


class RealestateEstate(models.Model):

    _inherit = "real.estate"

    analytic_account_id = fields.Many2one(comodel_name="account.analytic.account",)

    def button_analytic_entries(self):
        return {
            "name": _("Analytic Entries"),
            "view_mode": "tree,form",
            "res_model": "account.analytic.line",
            "view_id": False,
            "type": "ir.actions.act_window",
            "domain": [("account_id", "in", self.mapped("analytic_account_id").ids)],
        }
