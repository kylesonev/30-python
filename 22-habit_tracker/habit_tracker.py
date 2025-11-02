from dataclasses import dataclass
from datetime import datetime


@dataclass
class Habit:
    """
    Representa o progresso e os benefícios acumulados de um hábito.

    Attributes:
        name (str): Nome do hábito sendo acompanhado
        time_since (str): Tempo decorrido desde o início do hábito, em horas ou dias
        remaining_days (str): Quantidade de dias restantes para completar o objetivo (ou "Completo!")
        minutes_saved (float): Total de minutos poupados desde o início do hábito
        money_saved (str): Valor total economizado (considerando custo diário e valor do tempo poupado)
    """

    name: str
    time_since: str
    remaining_days: str
    minutes_saved: float
    money_saved: str


def track_habit(name: str, start: datetime, cost: float, minutes_used: float) -> Habit:
    """Calcula o progresso e os ganhos associados à manutenção de um hábito.

    Args:
        name (str): Nome do hábito (ex: "Parar de fumar", "Evitar delivery")
        start (datetime): Data e hora de início do hábito
        cost (float): Custo diário evitado ao manter o hábito
        minutes_used (float): Tempo médio diário (em minutos) que costumava ser gasto com o hábito

    Returns:
        Habit: Um objeto 'Habit' contendo o progresso atual, tempo decorrido,
        minutos poupados e dinheiro economizado.
    """
    goal: int = 60
    hourly_wage: int = 30

    time_elapsed: float = (datetime.now() - start).total_seconds()
    hours: float = round(time_elapsed / 60 / 60, 1)
    days: float = round(hours / 24, 2)

    money_saved: float = cost * days
    minutes_saved: float = round(days * minutes_used)
    total_money_saved: str = (
        f"R$ ({round(money_saved + (minutes_saved / 60 * hourly_wage), 2)})"
    )

    days_to_go: float | str = round(goal - days)

    remaining_days: str = "Completo!" if days_to_go <= 0 else f"{days_to_go}"

    time_since: str = f"{days} days" if hours >= 72 else f"{hours} hours"

    return Habit(
        name=name,
        time_since=time_since,
        remaining_days=remaining_days,
        minutes_saved=minutes_saved,
        money_saved=total_money_saved,
    )
