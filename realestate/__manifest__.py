# Copyright 2020 Denis Roussel
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Realestate",
    "summary": """
        Manages realestate""",
    "version": "13.0.1.0.0",
    "license": "AGPL-3",
    "author": "Denis Roussel, Odoo Community Association (OCA)",
    "website": "https://roussel-close.be",
    "depends": ["base", "mail", "contacts"],
    "data": [
        "security/security.xml",
        "views/menus.xml",
        "views/realestate_abstract_entity.xml",
    ],
    "application": True,
}
