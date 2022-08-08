from odoo import api, fields, models


"""This is the handle of the Comprobantes fiscales, allows the user to
Invervine and change or alter the sequence of the CF in question"""


class cf_sequence(models.Model):
    _name = "sequence.cf"

    name = fields.Char("name")
    l10n_latam_document_type_id = fields.Many2one("l10n_latam.document.type", String="Comprobante fiscal")
    current_sequence = fields.Integer("current_sequence", String="Secuencia actual")
    limit = fields.Integer("Limit", String="Limite")
    alarm_ncf = fields.Integer("alarm_ncf", String="Enviar aviso al llegar al número")

    @api.model
    def create(self, vals_list):
        if vals_list['limit'] == vals_list['current_sequence']:
            raise Exception("El limite no puede ser igual a la secuencia")
        id = super(cf_sequence, self).create(vals_list)
        return id

    def write(self, vals_list):
        id = super(cf_sequence, self).write(vals_list)

        return id


class SequenceMove(models.Model):
    _name = "sequence.cf.move"

    name = fields.Char("name")
    l10n_latam_document_type_id = fields.Many2one("l10n_latam.document.type", String="Comprobante fiscal")
    cf_sequence = fields.Many2one("cf.sequence")
    pos_order = fields.Many2one("pos.order")
    account_move = fields.Many2one("account.move")
