from app import app1
from app.models import Users
from flask import jsonify, request
from app import db



@app1.route("/users", methods=["GET"])
def get_users():
    users = Users.query.all()
    return jsonify([user.serialize() for user in users])
    # return jsonify(Users.query.all())

@app1.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = Users.query.where(Users.id == id).first()
    if user is None:
        return jsonify({})
    else:
        return jsonify(user.serialize())

@app1.route("/users", methods=["POST"])
def create_user():
    data = request.json
    user = Users(username=data['username'], name=data['name'], role=data['role'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return "Created successfully"

@app1.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.json
    user = Users.query.where(Users.id == id).first()

    for k, v in data.items():
        if (k == "password"):
            user.set_password(v)
        if k not in ["id", "password_hash", "role", "password"]:
            setattr(user, k, v)

    db.session.commit()

    return "Updated successully"

@app1.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = Users.query.where(Users.id == id).first()
    db.session.delete(user)
    db.session.commit()

    return "Deleted successully"