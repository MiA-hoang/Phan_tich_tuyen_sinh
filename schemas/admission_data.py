from marshmallow import Schema, fields, post_dump

class APIResponse(Schema):
    success = fields.Boolean(default=True)
    message = fields.String()
    data = fields.Dict(keys=fields.Str(), values=fields.Raw())  

class AdmissionScoreCreate(Schema):
    id = fields.String(required=True)
    major_id = fields.String(required=True)
    group_code = fields.String(required=True)
    year = fields.Integer(required=True)
    min_score = fields.Float(required=True)
    quota = fields.Integer()
    note = fields.String()

class AdmissionScoreUpdate(Schema):
    min_score = fields.Float()
    quota = fields.Integer()
    note = fields.String()

class AdmissionScoreResponse(Schema):
    Data_id = fields.Integer()
    id = fields.String()
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
    
def get_swagger_schema(schema_class):
    return schema_class().fields