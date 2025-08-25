from marshmallow import Schema, fields, post_dump

class APIResponse(Schema):
    success = fields.Boolean(default=True)
    message = fields.String()
    data = fields.Dict(keys=fields.Str(), values=fields.Raw())

class ExamGroupCreate(Schema):
    group_code = fields.String(required=True)
    description = fields.String(required=True)

class ExamGroupUpdate(Schema):
    description = fields.String()

class ExamGroupResponse(Schema):
    group_code = fields.String()
    description = fields.String()

    @post_dump
    def clean_output(self, data, **kwargs):
        if 'group_code' in data and isinstance(data['group_code'], str):
            data['group_code'] = data['group_code'].strip().upper()
        if 'description' in data and isinstance(data['description'], str):
            replacements = {
                "Toan": "Toán",
                "Ly": "Lý",
                "Hoa": "Hóa",
                "Van": "Văn",
                "Su": "Sử",
                "Dia": "Địa",
                "Anh": "Anh",
                "Sinh": "Sinh"
            }
            for ascii_text, unicode_text in replacements.items():
                data['description'] = data['description'].replace(ascii_text, unicode_text)
        return data
    
def get_swagger_schema(schema_class):
    return schema_class().fields