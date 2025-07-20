#!/usr/bin/env python3
"""
Author: Suhail Al-aboud
Email: 10675@holbertonstudents.com
"""

import logging
from typing import List, Dict, Any

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

def _safe_value(value: Any) -> str:
    """Return a printable value or 'N/A' when value is None/empty."""
    return str(value) if value not in (None, "") else "N/A"


def generate_invitations(template: str, attendees: List[Dict[str, Any]]) -> None:
    """
    Create personalized invitation files (output_#.txt) from a template.

    Args:
        template (str): Invitation text containing placeholders:
                        {name}, {event_title}, {event_date}, {event_location}
        attendees (List[Dict[str, Any]]): List of dictionaries with keys matching
                        the placeholders.

    Behavior:
        • Validates input types.
        • Handles empty template or attendee list.
        • Replaces missing/None values with 'N/A'.
        • Writes one file per attendee, numbered sequentially.
    """
    # ---------- Type validation ----------
    if not isinstance(template, str):
        logging.error("Invalid template type: expected str, got %s", type(template).__name__)
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error("Invalid attendees type: expected list of dicts")
        return

    # ---------- Empty‑value checks ----------
    if template.strip() == "":
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.warning("No data provided, no output files generated.")
        return

    # ---------- Generate files ----------
    for idx, attendee in enumerate(attendees, start=1):
        filled = template.format(
            name=_safe_value(attendee.get("name")),
            event_title=_safe_value(attendee.get("event_title")),
            event_date=_safe_value(attendee.get("event_date")),
            event_location=_safe_value(attendee.get("event_location")),
        )

        filename = f"output_{idx}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(filled)
            logging.info("Created %s", filename)
        except OSError as exc:
            logging.error("Failed to write %s: %s", filename, exc)
