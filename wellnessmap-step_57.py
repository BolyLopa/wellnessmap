# === Stage 57: Add structured result objects for command handlers ===
# Project: WellnessMap
from dataclasses import dataclass, field


@dataclass
class RoutineResult:
    """Structured result from a routine command handler."""
    routine_id: str
    name: str
    description: str = ""
    status: str = "pending"  # pending | active | completed | skipped
    next_run_at: float | None = None


@dataclass
class SymptomResult:
    """Structured result from a symptom command handler."""
    symptom_id: str
    name: str
    severity: int = 0        # 0-10
    tags: list[str] = field(default_factory=list)
    notes: str = ""


@dataclass
class MeasurementResult:
    """Structured result from a measurement command handler."""
    measurement_id: str
    name: str
    value: float | None = None
    unit: str = ""
    status: str = "ok"        # ok | warning | critical


@dataclass
class ReminderResult:
    """Structured result from a reminder command handler."""
    reminder_id: str
    title: str
    message: str = ""
    scheduled_at: float | None = None
    completed: bool = False


@dataclass
class TrendSummaryResult:
    """Structured result from a trend summary command handler."""
    metric_name: str
    data_points: list[dict] = field(default_factory=list)
    average_value: float | None = None
    min_value: float | None = None
    max_value: float | None = None
    trend_direction: str = "stable"  # rising | falling | stable


@dataclass
class WellnessMapResult:
    """Top-level result that can hold any command outcome."""
    kind: str                 # routine | symptom | measurement | reminder | trend
    success: bool = True
    error_message: str = ""
    payload: dict = field(default_factory=dict)

    def __post_init__(self):
        self.payload.setdefault("kind", self.kind)
