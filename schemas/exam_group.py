from marshmallow import Schema, fields

class ExamGroupCreateSchema(Schema):
    group_code = fields.String(required=True)
    description = fields.String(required=True)

class ExamGroupUpdateSchema(Schema):
    description = fields.String(required=True)

class ExamGroupResponseSchema(Schema):
    group_code = fields.String()
    description = fields.String()