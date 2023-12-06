from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=3, max=100))
    password = fields.Str(required=True, validate=validate.Length(min=8, max=100))
    role = fields.Str(required=True, validate=validate.OneOf(["admin", "user"]))

class AccountSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    balance = fields.Float(required=True, validate=validate.Range(min=0))
    user_id = fields.Int(required=True, validate=validate.Range(min=1))

class TransactionSchema(Schema):
    id = fields.Int(dump_only=True)
    sender_id = fields.Int(required=True, validate=validate.Range(min=1))
    receiver_id = fields.Int(required=True, validate=validate.Range(min=1))
    amount = fields.Float(required=True, validate=validate.Range(min=0))
    date = fields.DateTime(dump_only=True)
