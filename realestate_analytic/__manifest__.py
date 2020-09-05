# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Realestate Analytic",
    "summary": """
        Allows to link an analytic account to realestate objects""",
    "version": "13.0.1.0.0",
    "license": "AGPL-3",
    "development_status": "Alpha",
    "maintainers": ["rousseldenis"],
    "author": "ACSONE SA/NV,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/vertical-realestate",
    "depends": ["analytic", "realestate_estate"],
    "data": ["views/realestate_estate.xml", "views/analytic_account.xml"],
    "demo": ["demo/realestate_estate.xml"],
}
