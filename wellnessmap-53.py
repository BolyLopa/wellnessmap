# === Stage 53: Add command help text and usage examples ===
# Project: WellnessMap
def print_help():
    """Print usage instructions and a quick example for WellnessMap."""
    print("WellnessMap – Usage")
    print("=" * 30)
    print("1. Add measurements:")
    print("   import wellnessmap; w = wellnessmap.WellnessMap(); w.add_measurement('sleep', '8h')")
    print("2. Log a symptom:")
    print("   w.add_symptom('headache', severity='mild')")
    print("3. Define a routine:")
    print("   w.add_routine('Morning', ['meditate 10min', 'drink water'])")
    print("4. Set reminders:")
    print("   w.set_reminder('Take vitamin D', '08:00')")
    print("5. View trends:")
    print("   print(w.get_trend_summary())")
    print("6. Generate report:")
    print("   print(w.generate_report())")
