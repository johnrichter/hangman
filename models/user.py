from models import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)

    hosted_games = db.relationship('Game',
                                   primaryjoin='and_(User.id==Game.host_id)',
                                   backref='host',
                                   lazy='dynamic')
    played_games = db.relationship('Game',
                                   primaryjoin='and_(User.id==Game.player_id)',
                                   backref='player',
                                   lazy='dynamic')
    won_games = db.relationship('Game',
                                primaryjoin='and_(User.id==Game.winner_id)',
                                backref='winner',
                                lazy='dynamic')
    lost_games = db.relationship('Game',
                                 primaryjoin='and_(User.id==Game.loser_id)',
                                 backref='loser',
                                 lazy='dynamic')

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return 'User: %s' % self.username
