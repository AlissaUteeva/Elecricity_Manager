import pandas as pd


def load_data(filepath):
    """Загружаем данные из CSV."""
    return pd.read_csv(filepath)


def calculate_costs(df, rate):
    """Считаем суммы и стоимость."""
    # Сумма по приборам
    device_totals = df.groupby('device')['kwh'].sum().reset_index()
    device_totals = device_totals.sort_values(by='kwh', ascending=False)

    # Добавляем стоимость
    device_totals['cost'] = device_totals['kwh'] * rate

    total_cost = df['kwh'].sum() * rate
    return device_totals, total_cost


def get_top_5(device_totals):
    """Возвращает топ-5 приборов."""
    return device_totals.head(5)


def generate_markdown(device_totals, total_cost, rate, top_device):
    """Генерирует текст отчета в Markdown."""
    lines = []
    lines.append("# Отчет по потреблению электроэнергии\n")
    lines.append(f"**Тариф:** {rate} руб/кВт*ч\n")
    lines.append(f"**Общая стоимость:** {total_cost:.2f} руб.\n")
    lines.append("## Детализация по приборам\n")
    lines.append("| Прибор | Потребление (кВт*ч) | Стоимость (руб) |")
    lines.append("|---|---|---|")
    for _, row in device_totals.iterrows():
        lines.append(f"| {row['device']} | {row['kwh']:.2f} | {row['cost']:.2f} |")

    lines.append("\n## Выводы\n")
    lines.append(f"Основной расход электроэнергии дает **{top_device['device']}** "
                 f"({top_device['kwh']:.2f} кВт*ч).")
    return "\n".join(lines)