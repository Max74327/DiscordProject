import sqlalchemy
from .db_session import SqlAlchemyBase


class Player(SqlAlchemyBase):
    __tablename__ = 'players'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    hp = sqlalchemy.Column(sqlalchemy.Integer)
    strength = sqlalchemy.Column(sqlalchemy.Integer)
    dexterity = sqlalchemy.Column(sqlalchemy.Integer)
    constitution = sqlalchemy.Column(sqlalchemy.Integer)
    intellegence = sqlalchemy.Column(sqlalchemy.Integer)
    wisdom = sqlalchemy.Column(sqlalchemy.Integer)
    charisma = sqlalchemy.Column(sqlalchemy.Integer)
    modifier = sqlalchemy.Column(sqlalchemy.ARRAY(sqlalchemy.Integer))
    secondary_modifier = sqlalchemy.Column(sqlalchemy.ARRAY(sqlalchemy.Boolean))
    level = sqlalchemy.Column(sqlalchemy.Integer)
    xp = sqlalchemy.Column(sqlalchemy.Integer)
    chr_class = sqlalchemy.Column(sqlalchemy.Integer)
    armor = sqlalchemy.Column(sqlalchemy.Integer)
