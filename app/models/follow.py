from app import db 

class Follow(db.Model):
    __tablename__ = "follows"
    __table_args__ = {'schema': 'db_flask'}

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    userFollower = db.relationship('User', foreign_keys=follower_id, backref='follower')
    userFollowed = db.relationship('User', foreign_keys=followed_id, backref='followed')

    def __init__(self, follower_id, followed_id):
        self.follower_id = follower_id
        self.followed_id = followed_id
    
    def __repr__(self):
        return "<Follow %r>" % self.id