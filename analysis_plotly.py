import plotly.express as px
import pandas as pd
from base_model import get_session, User


# График участников по регионам
def plot_location_distribution():
    session = get_session()
    locations = [user.Location for user in session.query(User).all()]
    df = pd.DataFrame(locations, columns=['Регион'])
    fig = px.histogram(df, x='Регион', title='Распределение по регионам')
    fig.show()


# Зависимость пола и типа связи
def plot_gender_vs_communication():
    session = get_session()
    data = [(user.Gender, user.Preferred_Communication) for user in session.query(User).all()]
    if data:
        df = pd.DataFrame(data, columns=['Пол', 'Тип связи'])
        fig = px.bar(df.groupby(['Пол', 'Тип связи']).size().reset_index(name='Количество'),
                     x='Пол', y='Количество', color='Тип связи', barmode='group',
                     title='Зависимость пола и типа связи')
        fig.show()
    else:
        print('Нет данных для построения графика.')


# График частоты использования по регионам
def plot_frequency_by_location():
    session = get_session()
    data = [(user.Location, user.Usage_Frequency) for user in session.query(User).all()]
    if data:
        df = pd.DataFrame(data, columns=['Регион', 'Частота использования'])
        fig = px.histogram(df, x='Регион', color='Частота использования', barmode='group', title='Частота использования по регионам')
        fig.show()
    else:
        print('Нет данных для построения графика.')