import importlib


while True:
    print("Выберите библиотеку для визуализации:")
    print("1. Matplotlib")
    print("2. Seaborn")
    print("3. Plotly")
    print("4. Завершить программу")

    choice = input("Введите ваш выбор: ")

    if choice == '1':
        analysis = importlib.import_module('analysis_matplotlib')
        print("1. Построить график распределения по полу")
        print("2. Построить график частоты использования")
        print("3. Построить график предпочтений связи")
        sub_choice = input("Введите ваш выбор: ")

        if sub_choice == '1':
            analysis.plot_gender_distribution()
        elif sub_choice == '2':
            analysis.plot_usage_frequency()
        elif sub_choice == '3':
            analysis.plot_preferred_communication()
        else:
            print("Неверный выбор. Попробуйте снова.")

    elif choice == '2':
        analysis = importlib.import_module('analysis_seaborn')
        print("1. Построить график распределения образования")
        print("2. Построить график Зависимость пола и типа связи")
        print("3. Построить график связи уровня образования и частоты использования")
        sub_choice = input("Введите ваш выбор: ")

        if sub_choice == '1':
            analysis.plot_education_distribution()
        elif sub_choice == '2':
            analysis.plot_gender_vs_communication()
        elif sub_choice == '3':
            analysis.plot_education_vs_frequency()
        else:
            print("Неверный выбор. Попробуйте снова.")

    elif choice == '3':
        analysis = importlib.import_module('analysis_plotly')
        print("1. Построить график распределения по регионам")
        print("2. Построить график Зависимости пола и типа связи")
        print("3. Построить график зависимости частоты использования от регионов")
        sub_choice = input("Введите ваш выбор: ")

        if sub_choice == '1':
            analysis.plot_location_distribution()
        elif sub_choice == '2':
            analysis.plot_gender_vs_communication()
        elif sub_choice == '3':
            analysis.plot_frequency_by_location()
        else:
            print("Неверный выбор. Попробуйте снова.")
