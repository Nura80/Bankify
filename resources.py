from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, User, Account, Transaction
from datetime import datetime

class UserResource(Resource):
    @jwt_required()
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return {"id": user.id, "username": user.username, "role": user.role}

class AccountResource(Resource):
    @jwt_required()
    def get(self, account_id):
        account = Account.query.get_or_404(account_id)
        return {"id": account.id, "name": account.name, "balance": account.balance, "user_id": account.user_id}

class TransactionResource(Resource):
    @jwt_required()
    def get(self, transaction_id):
        transaction = Transaction.query.get_or_404(transaction_id)
        return {"id": transaction.id, "sender_id": transaction.sender_id, "receiver_id": transaction.receiver_id, "amount": transaction.amount, "date": transaction.date}

    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("sender_id", type=int, required=True)
        parser.add_argument("receiver_id", type=int, required=True)
        parser.add_argument("amount", type=float, required=True)
        args = parser.parse_args()

        sender_account = Account.query.get_or_404(args["sender_id"])
        receiver_account = Account.query.get_or_404(args["receiver_id"])

        if sender_account.balance < args["amount"]:
            return {"message": "Insufficient funds in the sender's account"}, 400

        new_transaction = Transaction(sender_id=args["sender_id"], receiver_id=args["receiver_id"], amount=args["amount"])
        sender_account.balance -= args["amount"]
        receiver_account.balance += args["amount"]

        db.session.add(new_transaction)
        db.session.commit()

        return {"id": new_transaction.id, "sender_id": new_transaction.sender_id, "receiver_id": new_transaction.receiver_id, "amount": new_transaction.amount, "date": new_transaction.date}, 201
