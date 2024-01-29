from app import db

class Post(db.Model):
    __tablename__: "posts"
    __table_args__ = {'schema': 'db_flask'}

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id
    
    def __repr__(self):
        return "<Post %r>" % self.id
    
    