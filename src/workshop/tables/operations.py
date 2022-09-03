import sqlalchemy as sa

from ..database import Base


class Operation(Base):
    __tablename__ = 'operations'

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    date = sa.Column(sa.Date)
    kind = sa.Column(sa.String)
    amount = sa.Column(sa.Numeric(10, 2)) # точность 10 знаков, 2 знака после запятой
    description = sa.Column(sa.String, nullable=True)
