# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: WellnessMap
import sys


def handle_keyboard_interrupt():
    """Catch Ctrl+C in the CLI and exit cleanly."""
    try:
        main()
    except KeyboardInterrupt:
        print("\nWellnessMap interrupted – exiting gracefully.")
        sys.exit(0)
