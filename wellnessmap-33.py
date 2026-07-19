# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: WellnessMap
DEFAULT_SETTINGS = {
    "units": {"weight": "kg", "height": "cm", "temperature": "°C"},
    "reminder_time": "09:00",
    "timezone": "UTC",
    "notifications_enabled": True,
    "default_routine_duration_minutes": 30,
}

def get_setting(key):
    return DEFAULT_SETTINGS.get(key)

def set_settings(settings_dict):
    global DEFAULT_SETTINGS
    for key, value in settings_dict.items():
        if key not in DEFAULT_SETTINGS:
            raise ValueError(f"Unknown setting: {key}")
        DEFAULT_SETTINGS[key] = value
