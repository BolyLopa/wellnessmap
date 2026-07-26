# === Stage 55: Add a setting to disable colorized output ===
# Project: WellnessMap
import os, sys


def disable_color_output():
    """Disables ANSI color codes in terminal output."""
    try:
        os.environ["NO_COLOR"] = "1"
        if hasattr(sys.stdout, "isatty") and not sys.stdout.isatty():
            return
        print("Color output disabled. Terminal is not a TTY or NO_COLOR is set.")
    except Exception as e:
        print(f"Error disabling color output: {e}")


if __name__ == "__main__":
    disable_color_output()
