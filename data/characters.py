
import sqlalchemy
from .db_session import SqlAlchemyBase


class Character(SqlAlchemyBase):
    __tablename__ = 'characters'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    strength = sqlalchemy.Column(sqlalchemy.Integer)
    dexterity = sqlalchemy.Column(sqlalchemy.Integer)
    constitution = sqlalchemy.Column(sqlalchemy.Integer)
    intelligence = sqlalchemy.Column(sqlalchemy.Integer)
    wisdom = sqlalchemy.Column(sqlalchemy.Integer)
    charisma = sqlalchemy.Column(sqlalchemy.Integer)
    username = sqlalchemy.Column(sqlalchemy.String)
    '''clss = sqlalchemy.Column(sqlalchemy.String)'''
    inventory = sqlalchemy.Column(sqlalchemy.String)
    inventory_weight = sqlalchemy.Column(sqlalchemy.Integer)
    max_inventory_weight = sqlalchemy.Column(sqlalchemy.Integer)
    xp = sqlalchemy.Column(sqlalchemy.Integer)
    level = sqlalchemy.Column(sqlalchemy.Integer)