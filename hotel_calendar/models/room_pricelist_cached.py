# Copyright 2018 Alexandre Díaz <dev@redneboa.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class RoomPricelistCached(models.Model):
    '''
    Cached Pricelist. Used only for Calendar Values
    '''

    _name = 'room.pricelist.cached'

    room_id = fields.Many2one('hotel.room.type', 'Virtual Room',
                              required=True, track_visibility='always')
    price = fields.Float('Price', default=0.0)
    date = fields.Date('Date', required=True, track_visibility='always')
