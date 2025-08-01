from marshmallow import Schema, fields, post_dump

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

    @post_dump
    def strip_fields(self, data, **kwargs):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = value.strip()
        return data
