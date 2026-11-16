import matplotlib.pyplot as plt


def plot_top_5(top_5_data, output_file='top_5_devices.png'):
    """Строим и сохраняем график топ-5."""
    plt.figure(figsize=(10, 6))
    plt.bar(top_5_data['device'], top_5_data['kwh'], color='skyblue')
    plt.title('Топ-5 приборов по потреблению (кВт*ч)')
    plt.xlabel('Прибор')
    plt.ylabel('Потребление (кВт*ч)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.savefig(output_file)
    print(f"График сохранен как '{output_file}'")
    plt.close()