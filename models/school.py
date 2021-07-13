from odoo import models, fields

SELECT_TYPE = [('public', 'Public School'), ('private', 'Private School')]


class SchoolProfile(models.Model):
    _name = "school.profile"
    name = fields.Char("School Name")
    email = fields.Char("Email")
    phone = fields.Char("Phone")
    is_virtual = fields.Boolean(string="Virtual class support?")
    rank = fields.Integer("Rank")
    result = fields.Float("Result")
    address = fields.Text("Address")
    establish_date = fields.Date(string="Established Date", invisible='1')
    open_date = fields.Datetime("Open Date", default=fields.Datetime.now())
    school_type = fields.Selection(SELECT_TYPE)
    school_image = fields.Image(string="Image", max_width=100, max_height=100, widget='image')
