from odoo import http
from odoo.addons.portal.controllers.mail import _message_post_helper


class PortalRequestChatter(http.Controller):

    # Based on /mail/chatter_post
    # implemented to avoid html escapes
    @http.route(['/mail/request_chatter_post'], type='http',
                methods=['POST'], auth='public', website=True)
    def portal_request_chatter_post(self, res_model, res_id, message, **kw):
        url = http.request.httprequest.referrer
        if message:
            # message is received in plaintext and saved in html
            # message = plaintext2html(message)

            if kw.get('pid'):
                # Enforce covertion of 'pid' param to int if present
                # This is needed to bypass bug in odoo code, that try to
                # browse partner record with string ID. So, this way,
                # we can ensure that everything will work fine.
                kw = dict(kw, pid=int(kw['pid']))
            _message_post_helper(res_model, int(res_id), message, **kw)
            url = url + "#discussion"
        return http.request.redirect(url)
