import plotly.express as px
from base_model import fetch_data


def plot_location_distribution():
    """
    Строит график распределения пользователей по регионам.
    """
    data = fetch_data(columns=["Location"])
    if not data.empty:
        fig = px.histogram(data, x='Location', title='Распределение по регионам')
        fig.update_layout(
            xaxis_title="Регион",
            yaxis_title="Количество пользователей"
        )
        fig.show()
    else:
        print('Нет данных для построения графика.')


def plot_gender_vs_communication():
    """
    Строит график зависимости пола и типа связи.
    """
    data = fetch_data(columns=["Gender", "Preferred_Communication"])
    if not data.empty:
        grouped_data = data.groupby(['Gender', 'Preferred_Communication']).size().reset_index(name='Количество')
        fig = px.bar(grouped_data, x='Gender', y='Количество', color='Preferred_Communication', barmode='group',
        title='Зависимость пола и типа связи', labels={
            'Gender': 'Пол',  # название для оси X
            'Preferred_Communication': 'Тип связи',  # название для легенды
            'Количество': 'Количество пользователей'  # название для оси Y
        })
        fig.show()
    else:
        print('Нет данных для построения графика.')


def plot_frequency_by_location():
    """
    Строит график зависимости частоты использования по регионам.
    """
    data = fetch_data(columns=["Location", "Usage_Frequency"])
    if not data.empty:
        fig = px.histogram(data, x='Location', color='Usage_Frequency', barmode='group',
                           title='Частота использования по регионам')
        fig.update_layout(
            xaxis_title="Регион",
            yaxis_title="Количество пользователей")
        fig.show()
    else:
        print('Нет данных для построения графика.')
