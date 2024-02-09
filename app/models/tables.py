from app import db

class User(db.Model):
    __tablename__= 'users'
    __table_args__ = {'schema': 'db_flask'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    #posts = db.relationship('Post', back_populates='post',  primaryjoin="users.id == posts.user_id")
    
    def __init__(self, name, username, password, email):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
    
    def __repr__(self):
        return "<User %r>" % self.username
   

class Post(db.Model):
    __tablename__ = 'posts'
    __table_args__ = {'schema': 'db_flask'}

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    #user = db.relationship('User', back_populates='post')

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id
    
    def __repr__(self):
        return "<Post %r>" % self.id
    
    
class Follow(db.Model):
    __tablename__ = 'follows'
    __table_args__ = {'schema': 'db_flask'}

    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    #userFollower = db.relationship('User', foreign_keys=follower_id, backref='follower')
    #userFollowed = db.relationship('User', foreign_keys=followed_id, backref='followed')

    def __init__(self, follower_id, followed_id):
        self.follower_id = follower_id
        self.followed_id = followed_id
    
    def __repr__(self):
        return "<Follow %r>" % self.id