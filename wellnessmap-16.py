# === Stage 16: Add argparse support for the most common commands ===
# Project: WellnessMap
import argparse


def main():
    parser = argparse.ArgumentParser(description="WellnessMap CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_routine = sub.add_parser("routine")
    p_routine.add_argument("--add", help="Add a routine")
    p_routine.add_argument("--list", action="store_true")
    p_routine.set_defaults(func=lambda _: print("Routines not implemented yet"))

    p_symptom = sub.add_parser("symptom")
    p_symptom.add_argument("--log", help="Log a symptom")
    p_symptom.add_argument("--list", action="store_true")
    p_symptom.set_defaults(func=lambda _: print("Symptoms not implemented yet"))

    p_measure = sub.add_parser("measure")
    p_measure.add_argument("--record", help="Record a measurement")
    p_measure.add_argument("--summary", action="store_true")
    p_measure.set_defaults(func=lambda _: print("Measurements not implemented yet"))

    p_reminder = sub.add_parser("reminder")
    p_reminder.add_argument("--set", nargs=2, metavar=("TYPE", "TIME"), help="Set a reminder")
    p_reminder.add_argument("--list", action="store_true")
    p_reminder.set_defaults(func=lambda _: print("Reminders not implemented yet"))

    p_trend = sub.add_parser("trend")
    p_trend.add_argument("--show", choices=["routine", "symptom", "measure"], required=True)
    p_trend.set_defaults(func=lambda _: print("Trends not implemented yet"))

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)


if __name__ == "__main__":
    main()
