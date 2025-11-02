from datetime import datetime

import pandas as pd
from tabulate import tabulate

from habit_tracker import Habit, track_habit


def main():
    """
    Executa o rastreamento de hábitos e exibe os resultados em formato tabular.
    """
    habits: list[Habit] = [
        track_habit("Café", datetime(2025, 4, 4, 8), cost=1, minutes_used=5)
    ]

    df = pd.DataFrame(habits)

    print(tabulate(df, headers="keys", tablefmt="psql"))


if __name__ == "__main__":
    main()
