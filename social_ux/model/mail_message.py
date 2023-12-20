# -*- coding: utf-8 -*-

from odoo import models, _
from odoo.exceptions import UserError

class Message(models.Model):
    _inherit = 'mail.message'
    
    def write(self, vals):
        if 'body' in vals and not self.user_has_groups("social_ux.group_edit_delete_message"):
            raise UserError("No es posible editar o eliminar esta nota")
        return super(Message, self).write(vals)
