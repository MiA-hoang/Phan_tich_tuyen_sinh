from marshmallow import Schema, fields

class UniversityCreateSchema(Schema):
    id = fields.String(required=True)
    name = fields.String(required=True)
    type = fields.String(required=True)     
    city = fields.String(required=True)
    region = fields.String(required=True)

class UniversityUpdateSchema(Schema):
    name = fields.String()
    type = fields.String()                 
    city = fields.String()
    region = fields.String()

class UniversityResponseSchema(Schema):
    id = fields.String()
    name = fields.String()
    type = fields.String()                   
    city = fields.String()
    region = fields.String()