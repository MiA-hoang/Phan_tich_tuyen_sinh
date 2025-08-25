from marshmallow import Schema, fields, post_dump

class APIResponse(Schema):
    success = fields.Boolean(default=True)
    message = fields.String()
    data = fields.Dict(keys=fields.Str(), values=fields.Raw())  

class UniversityCreate(Schema):
    id = fields.String(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True)
    city = fields.String(required=True)
    region = fields.String(required=True)

class UniversityUpdate(Schema):
    name = fields.String()
    type = fields.String()
    city = fields.String()
    region = fields.String()

class UniversityResponse(Schema):
    id = fields.String()
    name = fields.String()
    type = fields.String()
    city = fields.String()
    region = fields.String()

    @post_dump
    def strip_fields(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()
        return data
    
def get_swagger_schema(schema_class):
    return schema_class().fields