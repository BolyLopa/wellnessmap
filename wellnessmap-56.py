# === Stage 56: Add compact error classes for domain failures ===
# Project: WellnessMap
class WellnessError(Exception): pass
class RoutineNotFoundError(WellnessError): pass
class SymptomMismatchError(WellnessError): pass
class MeasurementOutOfRangeError(WellnessError): pass
class ReminderConflictError(WellnessError): pass
class TrendDataInconsistentError(WellnessError): pass
