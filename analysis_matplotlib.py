import matplotlib.pyplot as plt
from base_model import get_session, User


# График распределения возрастов
def plot_age_distribution():
    session = get_session()
    ages = [user.Age for user in session.query(User).all()]
    plt.hist(ages, bins=10, color='blue', alpha=0.7)
    plt.title('Распределение возрастов')
    plt.xlabel('Возраст')
    plt.ylabel('Количество')
    plt.show()


# График гендерного распределения
def plot_gender_distribution():
    session = get_session()
    genders = [user.Gender for user in session.query(User).all()]
    plt.bar(*zip(*{gender: genders.count(gender) for gender in set(genders)}.items()), color='green')
    plt.title('Распределение по полу')
    plt.xlabel('Пол')
    plt.ylabel('Количество')
    plt.show()


# График частоты использования
def plot_usage_frequency():
    session = get_session()
    frequencies = [user.Usage_Frequency for user in session.query(User).all()]
    plt.bar(*zip(*{freq: frequencies.count(freq) for freq in set(frequencies)}.items()), color='orange')
    plt.title('Частота использования')
    plt.xlabel('Частота')
    plt.ylabel('Количество')
    plt.show()


# График предпочтений связи
def plot_preferred_communication():
    session = get_session()
    communications = [user.Preferred_Communication for user in session.query(User).all()]
    plt.bar(*zip(*{comm: communications.count(comm) for comm in set(communications)}.items()), color='purple')
    plt.title('Предпочитаемый способ связи')
    plt.xlabel('Способ связи')
    plt.ylabel('Количество')
    plt.show()