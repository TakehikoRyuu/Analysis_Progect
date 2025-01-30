import matplotlib.pyplot as plt
from base_model import fetch_data


def plot_gender_distribution():
    """
    Строит гистограмму распределения пользователей по полу.
    """
    data = fetch_data(columns=["Gender"])
    item_counts = data["Gender"].value_counts()
    plt.bar(item_counts.index, item_counts.values, color='green')
    plt.title('Распределение по полу')
    plt.xlabel('Пол')
    plt.ylabel('Количество')
    plt.show()


def plot_usage_frequency():
    """
    Строит гистограмму распределения пользователей по частоте использования приложения.
    """
    data = fetch_data(columns=["Usage_Frequency"])
    item_counts = data["Usage_Frequency"].value_counts()
    plt.bar(item_counts.index, item_counts.values, color='orange')
    plt.title('Частота использования')
    plt.xlabel('Частота')
    plt.ylabel('Количество')
    plt.show()


def plot_preferred_communication():
    """
    Строит гистограмму распределения пользователей по предпочтений связи.
    """
    data = fetch_data(columns=["Gender"])
    item_counts = data["Gender"].value_counts()
    plt.bar(item_counts.index, item_counts.values, color='purple')
    plt.title('Предпочитаемый способ связи')
    plt.xlabel('Способ связи')
    plt.ylabel('Количество')
    plt.show()
