from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    g2p_home_menu_background_image = fields.Binary(
        related="company_id.g2p_home_menu_background_image",
        readonly=False,
    )
