import seaborn as sns
import matplotlib.pyplot as plt
from base_model import fetch_data


def plot_education_distribution():
    """
    Строит график распределения пользователей по уровню образования.
    """
    data = fetch_data(columns=["Education"])
    if not data.empty:
        sns.countplot(y="Education", data=data, hue="Education", palette='coolwarm', legend=False)
        plt.title('Распределение по уровню образования')
        plt.xlabel('Количество')
        plt.ylabel('Образование')
        plt.legend([], [], frameon=False)
        plt.show()
    else:
        print('Нет данных для построения графика.')


def plot_gender_vs_communication():
    """
    Строит график зависимости пола и предпочтительного типа связи.
    """
    data = fetch_data(columns=["Gender", "Preferred_Communication"])
    if not data.empty:
        sns.countplot(x='Gender', hue='Preferred_Communication', data=data, palette='coolwarm')
        plt.title('Зависимость пола и типа связи')
        plt.xlabel('Пол')
        plt.ylabel('Количество')
        plt.legend(title='Тип связи')
        plt.show()
    else:
        print('Нет данных для построения графика.')


def plot_education_vs_frequency():
    """
    Строит график зависимости уровня образования и частоты использования.
    """
    data = fetch_data(columns=["Education", "Usage_Frequency"])
    if not data.empty:
        sns.countplot(x='Education', hue='Usage_Frequency', data=data, palette='viridis')
        plt.title('Связь уровня образования и частоты использования')
        plt.xlabel('Образование')
        plt.ylabel('Частота использования')
        plt.legend(title='Частота использования')
        plt.show()
    else:
        print('Нет данных для построения графика.')
