# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: WellnessMap
if __name__ == "__main__":
    import sys, colorama
    if sys.platform != "win32":
        colorama.init()
        RESET = "\033[0m"
        BOLD  = "\033[1m"
        DIM   = "\033[2m"
        RED   = "\033[91m"
        GREEN = "\033[92m"
        YELLOW= "\033[93m"
        BLUE  = "\033[94m"
    else:
        RESET=BOLD=DIM=RED=GREEN=YELLOW=BLUE=""

    # demo of colorized output
    print(f"{BOLD}=== WellnessMap Demo ==={RESET}")
    for name, val in [("Heart rate", 78), ("Sleep hours", 7.5)]:
        status = "ok" if (val == 78 or val == 7.5) else "warn"
        color = GREEN if status == "ok" else YELLOW
        print(f"{BOLD}{name}{RESET}: {color}{DIM}→ {val} →{RESET}")

    print(f"\n{RED}Symptom: Migraine (stress-related){RESET}")
    print(f"\n{BLUE}Routine: Morning meditation — 5 min{RESET}")

    # ANSI color helper for future use
    def c(text, code): return f"{code}{text}{RESET}" if RESET else text
