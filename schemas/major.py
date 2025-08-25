from marshmallow import Schema, fields, post_dump

class APIResponse(Schema):
    success = fields.Boolean(default=True)
    message = fields.String()
    data = fields.Dict(keys=fields.Str(), values=fields.Raw())  

class MajorCreate(Schema):
    major_id = fields.String(required=True)
    name = fields.String(required=True)
    group_major = fields.String(required=True)

class MajorUpdate(Schema):
    name = fields.String()
    group_major = fields.String()

class MajorResponse(Schema):
    major_id = fields.String()
    name = fields.String()
    group_major = fields.String()

    @post_dump
    def strip_fields(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()
        return data

def get_swagger_schema(schema_class):
    return schema_class().fields