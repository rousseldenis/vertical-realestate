# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Realestate Contract",
    "summary": """
        Allows to link contracts to real estate""",
    "version": "13.0.1.0.0",
    "license": "AGPL-3",
    "author": "ACSONE SA/NV,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/vertical-realestate",
    "depends": ["contract", "realestate_estate"],
    "data": ["views/contract_contract.xml", "views/realestate_estate.xml"],
}
