from __future__ import annotations
from typing import List, Sequence
def _check_window(window: int, n: int) -> None:
    if not isinstance(window, int) or isinstance(window, bool):
        raise ValueError(f"window должно быть целым (получено: {window!r})")
    if window < 1:
        raise ValueError(f"window должно быть >= 1 (получено: {window})")
    if window > n:
        raise ValueError(
            f"window ({window}) не может быть больше длины ряда ({n})"
        )
def simple_moving_average(data: Sequence[float], window: int) -> List[float]:
    if not data:
        raise ValueError("Ряд пуст: расчёт SMA невозможен")
    _check_window(window, len(data))
    running = sum(data[:window])
    result = [running / window]
    for i in range(window, len(data)):
        running += data[i] - data[i - window]
        result.append(running / window)
    return result
def centered_moving_average(data: Sequence[float], window: int) -> List[float]:
    if not data:
        raise ValueError("Ряд пуст: расчёт CMA невозможен")
    _check_window(window, len(data))
    if window % 2 == 0:
        raise ValueError(
            f"Для центрированного MA окно должно быть нечётным (получено: {window})"
        )
    half = window // 2
    n = len(data)
    result = []
    for i in range(half, n - half):
        result.append(sum(data[i - half:i + half + 1]) / window)
    return result
def exponential_moving_average(data: Sequence[float], alpha: float) -> List[float]:
    """EMA: EMA[0] = data[0]; EMA[i] = alpha*x[i] + (1-alpha)*EMA[i-1]."""
    if not data:
        raise ValueError("Ряд пуст: расчёт EMA невозможен")
    if not (0 < alpha <= 1):
        raise ValueError(f"alpha должно быть в (0, 1] (получено: {alpha})")
    result = [float(data[0])]
    for i in range(1, len(data)):
        result.append(alpha * data[i] + (1 - alpha) * result[-1])
    return result