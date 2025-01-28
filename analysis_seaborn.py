import seaborn as sns
import matplotlib.pyplot as plt
from base_model import get_session, User
import pandas as pd


# График распределения образования
def plot_education_distribution():
    session = get_session()
    educations = [user.Education for user in session.query(User).all()]
    sns.countplot(y=educations, hue=educations, dodge=False, palette='coolwarm')
    plt.title('Распределение по уровню образования')
    plt.xlabel('Количество')
    plt.ylabel('Образование')
    plt.legend([], [], frameon=False)  # Убираем лишнюю легенду
    plt.show()


# Зависимость пола и типа связи
def plot_gender_vs_communication():
    session = get_session()
    data = [(user.Gender, user.Preferred_Communication) for user in session.query(User).all()]
    if data:
        df = pd.DataFrame(data, columns=['Пол', 'Тип связи'])
        sns.countplot(x='Пол', hue='Тип связи', data=df, palette='coolwarm')
        plt.title('Зависимость пола и типа связи')
        plt.xlabel('Пол')
        plt.ylabel('Количество')
        plt.legend(title='Тип связи')
        plt.show()
    else:
        print('Нет данных для построения графика.')


# График связи уровня образования и частоты использования
def plot_education_vs_frequency():
    session = get_session()
    data = [(user.Education, user.Usage_Frequency) for user in session.query(User).all()]
    if data:
        df = pd.DataFrame(data, columns=['Образование', 'Частота использования'])
        sns.countplot(x='Образование', hue='Частота использования', data=df, palette='viridis')
        plt.title('Связь уровня образования и частоты использования')
        plt.xlabel('Образование')
        plt.ylabel('Частота использования')
        plt.legend(title='Частота использования')
        plt.show()
    else:
        print('Нет данных для построения графика.')