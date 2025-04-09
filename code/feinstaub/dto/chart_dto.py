from dataclasses import dataclass


@dataclass
class ChartDustEntry:
    min_p1: float
    max_p1: float
    avg_p1: float
    min_p2: float
    max_p2: float
    avg_p2: float


@dataclass
class ChartWeatherEntry:
    min_temperature: float
    max_temperature: float
    avg_temperature: float
    min_pressure: float
    max_pressure: float
    avg_pressure: float
    min_humidity: float
    max_humidity: float
    avg_humidity: float
    altitude: float
    min_pressure_sealevel: float
    max_pressure_sealevel: float
    avg_pressure_sealevel: float
