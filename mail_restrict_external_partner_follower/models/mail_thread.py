
from odoo import models, _

class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    def _message_subscribe(self, partner_ids=None, subtype_ids=None, customer_ids=None):
        res = super(MailThread, self)._message_subscribe(partner_ids, subtype_ids, customer_ids)
        if self._name in ('sale.order','account.move','account.payment.group','purchase.order'):
            if self.partner_id.id in partner_ids:
                
                follower_record = self.env["mail.followers"].search([('res_model', '=', self._name),
                                                            ('res_id', '=', self.id),
                                                            ('partner_id', '=',self.partner_id.id)])

                follower_record.write({'subtype_ids': [(3, 1,_)]})

                
