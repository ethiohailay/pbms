from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    g2p_home_menu_background_image = fields.Binary(
        string="G2P Home Menu Image",
        attachment=True,
    )
