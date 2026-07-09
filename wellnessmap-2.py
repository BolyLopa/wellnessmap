# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: WellnessMap
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Symptom:
    name: str
    severity: int = 1          # 0..5
    notes: str = ""


@dataclass
class Measurement:
    value: float
    unit: str
    recorded_on: date = field(default_factory=date.today)


@dataclass
class Reminder:
    title: str
    scheduled_for: date = field(default_factory=date.today)
    done: bool = False


@dataclass
class Routine:
    name: str
    steps: list[str] = field(default_factory=list)
    frequency_days: int = 1
