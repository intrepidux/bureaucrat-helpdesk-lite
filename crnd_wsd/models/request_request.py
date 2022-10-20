import re
from odoo import models, fields


class RequestRequest(models.Model):
    _name = 'request.request'
    _inherit = [
        'request.request',
        'portal.mixin',
    ]
    _mail_post_access = 'read'

    # Set this to compute with sudo to avoid access rights conflicts
    activity_date_deadline = fields.Date(compute_sudo=True)
    created_by_avatar = fields.Binary(
        "Creator (Avatar)", related='created_by_id.image_small')
    author_avatar = fields.Binary(
        "Author (Avatar)", related='author_id.image_small')
    assignee_avatar = fields.Binary(
        "Assignee (Avatar)", related='user_id.image_small')
    closed_by_avatar = fields.Binary(
        "Closed By (Avatar)", related='closed_by_id.image_small')
    website_id = fields.Many2one('website', index=True)

    def _compute_access_url(self):
        res = super(RequestRequest, self)._compute_access_url()
        for request in self:
            request.access_url = '/requests/request/%s' % request.id
        return res

    def get_access_action(self, access_uid=None):
        """ Redirect portal users to website interface. """
        self.ensure_one()

        user, record = self.env.user, self
        if access_uid:
            user = self.env['res.users'].sudo().browse(access_uid)
            record = self.sudo(user)
        if user.share:
            return {
                'type': 'ir.actions.act_url',
                'url': record.access_url,
                'target': 'self',
                'res_id': self.id,
            }
        return super(RequestRequest, self).get_access_action(access_uid)

    def _request_bind_attachments(self):
        self.ensure_one()
        attachment_ids = []
        for m in re.finditer(r"/web/(?:content|image)/(\d+)/",
                             self.request_text):
            att_id = int(m[1])
            attachment_ids.append(att_id)

        self.env['ir.attachment'].search([
            ('res_model', '=', False),
            ('res_id', '=', False),
            ('id', 'in', attachment_ids),
        ]).sudo().write({
            'res_model': 'request.request',
            'res_id': self.id,
        })

    def _notify_get_groups(self, message, groups):
        """ Display access button in mails to portal users
        """
        self.ensure_one()
        groups = super(RequestRequest, self)._notify_get_groups(
            message, groups)

        # pylint: disable=unused-variable
        for group_name, group_method, group_data in groups:
            if group_name == 'customer':
                continue
            group_data['has_button_access'] = True

        return groups

    def get_mail_url(self, pid=None):
        if self.env.user.company_id.request_mail_link_access == 'shared-link':
            return self._get_share_url(redirect=True, pid=pid)
        return super().get_mail_url(pid=pid)

    def action_show_on_website(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'url': self.access_url,
            'target': 'self',
        }
