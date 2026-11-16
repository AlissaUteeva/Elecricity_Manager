import sys
import os
import pandas as pd

# Путь к папке
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

import core


def test_calculate_costs():
    # Создание тестовых данных
    data = {'device': ['A', 'A', 'B'], 'kwh': [1.0, 1.0, 2.0]}
    df = pd.DataFrame(data)

    # Расчет
    device_totals, total_cost = core.calculate_costs(df, rate=5.0)

    # Проверка результата
    assert total_cost == 20.0
    print("Тест calculate_costs пройден!")


def test_generate_markdown():
    # Создание тестовых данных
    data = {'device': ['ТВ'], 'kwh': [1.0], 'cost': [5.0]}
    df = pd.DataFrame(data)

    # Генерация отчета
    report = core.generate_markdown(df, total_cost=5.0, rate=5.0, top_device=df.iloc[0])

    # Проверяем, что в отчете есть нужные слова
    assert "# Отчет по потреблению" in report
    assert "ТВ" in report
    print("Тест generate_markdown пройден!")


if __name__ == "__main__":
    test_calculate_costs()
    test_generate_markdown()
    print("Все тесты успешно пройдены.")