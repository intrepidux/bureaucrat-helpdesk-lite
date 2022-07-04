from odoo import api, SUPERUSER_ID
from odoo.addons.generic_mixin.tools.migration_utils import ensure_version


@ensure_version('1.20.0')
def migrate(cr, installed_version):
    env = api.Environment(cr, SUPERUSER_ID, {})
    cron_job = env.ref(
        'generic_request.ir_cron_request_vacuum_events')
    cron_job.write({'code': 'model._scheduler_vacuum()'})
