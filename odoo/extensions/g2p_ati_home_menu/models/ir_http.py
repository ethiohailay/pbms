from odoo import models
from odoo.http import request


class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    def session_info(self):
        result = super().session_info()
        if request.env.user._is_internal():
            for company in request.env.user.company_ids.with_context(bin_size=True):
                result["user_companies"]["allowed_companies"][company.id].update(
                    {
                        "has_g2p_home_menu_background_image": bool(
                            company.g2p_home_menu_background_image
                        ),
                    }
                )
        return result
