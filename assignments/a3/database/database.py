from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from assignments.a3.database.base import base, Record


class Database:

    def __init__(self):
        engine = create_engine('sqlite:///database.db', echo=False)
        base.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine)()

    def get_record(self, record_id: int):
        record = self.session.query(Record).filter(Record.id == record_id).first()
        if record:
            return record.to_dict()
        return {}

    def get_records(self):
        result = self.session.query(Record).all()
        if result:
            return [record.to_dict() for record in result]
        return []

    def add_record(self, category: int, data1: float, data2: float):
        record = Record(category=category, data1=data1, data2=data2)
        self.session.add(record)
        self.session.commit()
        return record.id

    def delete_record(self, record_id: int):
        record = self.session.query(Record).filter(Record.id == record_id).first()
        if record:
            self.session.delete(record)
            self.session.commit()
            return record_id
        return None
