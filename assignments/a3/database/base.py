from sqlalchemy import Float, create_engine
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


class Record(base):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(Integer, nullable=False)
    data1 = Column(Float, nullable=False)
    data2 = Column(Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'category': self.category,
            'data1': self.data1,
            'data2': self.data2
        }
