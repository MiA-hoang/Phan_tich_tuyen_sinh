from marshmallow import Schema, fields, post_dump

class ExamGroupCreateSchema(Schema):
    group_code = fields.String(required=True)
    description = fields.String(required=True)

class ExamGroupUpdateSchema(Schema):
    description = fields.String()

class ExamGroupResponseSchema(Schema):
    group_code = fields.String()
    description = fields.String()

    @post_dump
    def clean_output(self, data, **kwargs):
        # 1. Xóa khoảng trắng ở group_code
        if 'group_code' in data and isinstance(data['group_code'], str):
            data['group_code'] = data['group_code'].strip().upper()

        # 2. Chuẩn hóa description nếu là chuỗi
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
