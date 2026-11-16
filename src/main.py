import os
import sys

# Путь к папке
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import core
import ui


def main():
    # Путь к данным
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'primer.csv')

    if not os.path.exists(data_path):
        print(f"Ошибка: Файл {data_path} не найден.")
        return

    # 1. Загрузка
    df = core.load_data(data_path)

    # 2. Ввод тарифа
    while True:
        try:
            rate_input = input("Введите тариф (руб/кВт*ч) [по умолчанию 5.5]: ")

            if not rate_input.strip():
                rate = 5.5
                break

            rate = float(rate_input)

            if rate <= 0:
                print("Ошибка, введите положительное число")
                continue

            break

        except ValueError:
            # Сюда попадаем, если ввели буквы
            print("Ошибка, введите корректное число, не буквы")

    # 3. Расчет
    device_totals, total_cost = core.calculate_costs(df, rate)
    top_5 = core.get_top_5(device_totals)
    top_device = device_totals.iloc[0]

    # 4. График
    ui.plot_top_5(top_5)

    # 5. Отчет
    report_text = core.generate_markdown(device_totals, total_cost, rate, top_device)
    with open('report.md', 'w', encoding='utf-8') as f:
        f.write(report_text)

    print("Отчет сохранен как 'report.md'")
    print(f"\nИтоговая стоимость: {total_cost:.2f} руб.")


if __name__ == "__main__":
    main()