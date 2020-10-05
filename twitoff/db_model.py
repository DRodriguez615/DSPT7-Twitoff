from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy()


class User(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    username = DB.Column(DB.String(80), unique=True, nullable=False)
    followers = DB.Column(DB.String(120), unique=True, nullable=False) 
    #Tweets IdDS are ordinal ints, so we can fetch most recent data
    newest_tweet_id = DB.Column(DB.BigInteger, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Tweet(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    tweet = DB.Column(DB.String(280), unique=True, nullable=False)
    embedding = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.Integer, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweet', lazy=True))

    def __repr__(self):
        return '<Tweet %r>' % self.tweet


# To create the database:
# FLASK_APP=twitoff:APP flask shell
# from twitoff.db_model import DB, User, Tweet
# DB.create_all()

# To add user:
# Example:
# u1 = User(username='name', followers=?(int))
# u1 (to see user name)
# DB.session.add(u1) (add user to db)
# DB.session.commit() (save user to db)

# Add tweet:
# tweet1 = Tweet(tweet="Sample tweet #awesome!", user=u1)
# DB.session.add(tweet1)
# DB.session.commit()


# QUERY functions: 
# Add tweet to user using filter_by:
# tweet2 = Tweet(tweet='Tesla stock soared today!', user=User.query.filter_by(username='Damon').first())

# See all users:
# User.query.all()