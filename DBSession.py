from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Girl(Base):
    __tablename__ = 'girl'

    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    address = Column(String(255))
    avatar = Column(String(255))


class Image(Base):
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(255))
    time = Column(String(20))
    uid = Column(Integer)


DB_CONNECT_STRING = 'mysql+mysqlconnector://root:shuai2016@localhost:3306/meizhi?charset=utf8mb4'
engine = create_engine(DB_CONNECT_STRING, convert_unicode=True)

DBSession = sessionmaker(bind=engine)
