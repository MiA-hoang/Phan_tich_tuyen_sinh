from marshmallow import Schema, fields, post_dump

class AdmissionScoreCreateSchema(Schema):
    university_id = fields.String(required=True)
    major_id = fields.String(required=True)
    group_code = fields.String(required=True)
    year = fields.Integer(required=True)
    min_score = fields.Float(required=True)
    quota = fields.Integer()
    note = fields.String()

class AdmissionScoreUpdateSchema(Schema):
    min_score = fields.Float()
    quota = fields.Integer()
    note = fields.String()

class AdmissionScoreResponseSchema(Schema):
    id = fields.Integer()
    university_id = fields.String()
    major_id = fields.String()
    group_code = fields.String()
    year = fields.Integer()
    min_score = fields.Float()
    quota = fields.Integer()
    note = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

    @post_dump
    def strip_fields(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()
        return data
