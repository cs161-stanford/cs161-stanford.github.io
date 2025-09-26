# one_time_convert.py
import json, pytz
from datetime import datetime, timedelta
from icalendar import Calendar
import recurring_ical_events

# change these for your quarter range
START = datetime(2025, 9, 29)
END   = datetime(2025, 12, 6)
TZ    = "America/Los_Angeles"

def to_iso(dt):
    if isinstance(dt, datetime):
        if dt.tzinfo is None:
            dt = pytz.timezone(TZ).localize(dt)
        return dt.isoformat()
    else:
        return dt.isoformat()

with open("oh.ics", "rb") as f:
    cal = Calendar.from_ical(f.read())

events = []
for ev in recurring_ical_events.of(cal).between(START, END):
    title = str(ev.get("summary", ""))
    loc   = str(ev.get("location", ""))
    desc  = str(ev.get("description", ""))
    dtstart = ev.decoded("dtstart")
    dtend   = ev.decoded("dtend", None)
    if dtend is None:
        dtend = dtstart + timedelta(hours=1)
    events.append({
        "title": title,
        "start": to_iso(dtstart),
        "end": to_iso(dtend),
        "extendedProps": { "location": loc, "description": desc }
    })

with open("events.json", "w") as f:
    json.dump(events, f, indent=2)
