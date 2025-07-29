from marshmallow import Schema, fields, pre_load

class AdmissionScoreCreateSchema(Schema):
    university_id = fields.String(required=True)
    major_id = fields.String(required=True)
    group_code = fields.String(required=True)
    year = fields.Integer(required=True)
    min_score = fields.Float(required=True)
    quota = fields.Integer(required=False)
    note = fields.String(required=False)

    @pre_load
    def strip_fields(self, data, **kwargs):
        for key in ['university_id', 'major_id', 'group_code']:
            if key in data and isinstance(data[key], str):
                data[key] = data[key].strip()
        return data


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
