from odoo import models, api


class MailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    @api.model
    def create(self, values):
        # Link here response attachments to composer
        composer = super(MailComposeMessage, self).create(values)
        attachments = values.get('attachment_ids', [])
        if attachments and composer.model == 'request.request':
            composer_attachments_ids = [
                (4, attachment.id) for attachment in attachments]
            composer.write({
                'attachment_ids': composer_attachments_ids,
            })
        return composer
