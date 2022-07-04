from odoo import api, SUPERUSER_ID
from odoo.addons.generic_mixin.tools.migration_utils import ensure_version


@ensure_version('1.14.0')
def migrate(cr, installed_version):
    env = api.Environment(cr, SUPERUSER_ID, {})
    request = env.ref(
        'generic_request.request_request_type_sequence_demo_1',
        raise_if_not_found=False)
    partner = env.ref(
        'base.res_partner_2',
        raise_if_not_found=False)

    if request and partner and request.partner_id != partner:
        request.partner_id = partner
