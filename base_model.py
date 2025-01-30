from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import pandas as pd

# Создаем базовый класс для моделей
Base = declarative_base()


# Определение таблицы Users
class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    Age = Column(Integer, nullable=False)
    Gender = Column(String, nullable=False)
    Location = Column(String)
    Education = Column(String)
    Occupation = Column(String)
    Usage_Frequency = Column(String)
    Daily_Usage_Time = Column(String)
    Preferred_Communication = Column(String)


def get_session():
    engine = create_engine('sqlite:///dating.db')
    Session = sessionmaker(bind=engine)
    return Session()


def fetch_data(columns):
    """
    Получает данные из БД и возвращает их в виде DataFrame.

    :param columns: Список столбцов, которые нужно получить.
    :return: DataFrame с данными.
    """
    session = get_session()
    query = session.query(*[getattr(User, col) for col in columns])
    data = [row._asdict() for row in query.all()]
    return pd.DataFrame(data)
