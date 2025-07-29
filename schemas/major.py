from marshmallow import Schema, fields

class MajorCreateSchema(Schema):
    major_id = fields.String(required=True)
    name = fields.String(required=True)
    group_major = fields.String(required=True)

class MajorUpdateSchema(Schema):
    name = fields.String()
    group_major = fields.String()

class MajorResponseSchema(Schema):
    major_id = fields.String()
    name = fields.String()
    group_major = fields.String()
