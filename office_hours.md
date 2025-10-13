---
layout: default
title: Office Hours
permalink: /office_hours/
---

# Office Hours

<div class="panel">
  <h5> Office Hours Overview </h5>
<ul>
  <li> Please use the follow link to hop on the office hours queue: <a href="https://queue.cs.stanford.edu/queues/33FZ7Pjm646CQAkIFshsyyYfm84" class="btn btn-danger" style="color: white !important;"> OH Queue Link </a>.</li>
	<li> The calendar below shows the office hour schedule.  We will mostly keep the same schedule each week, but make sure to check in case there are sporadic changes. Here is the <a href="https://calendar.google.com/calendar/u/2?cid=NzEwZWQ4N2VmNjlkYzZjOWNiNWFiNjkwYzdhMmI4MDIxNjFjN2Q5ZTQ3MWU2MTM3NTI3NmM2ZDAxNzNkYzVmZkBncm91cC5jYWxlbmRhci5nb29nbGUuY29t"> Google Calendar </a> link if you would like to add it to your own calendar.
</li>
	<li> Check each calendar event for office hour location. OH will be held in Huang basement; Mary's OH will be in CoDa W216.</li>
	<li> Office hours start in <b> Week 2. </b></li>
	<li> We will have a <b> Homework Party </b> on Monday evenings (generally in Huang basement) so you can work on HW with your friends and the CAs!  (Starting in Week 2).  <b> There will be pizza! </b>  Again, see the calendar information for the location, which may change week-to-week. </li>
</ul>
</div>

<div class="panel">

<link href="https://cdn.jsdelivr.net/npm/fullcalendar@6.1.19/main.min.css" rel="stylesheet" />
<div id="calendar" style="max-width:1100px;margin:20px auto;"></div>

<script src="https://cdn.jsdelivr.net/npm/fullcalendar@6.1.19/index.global.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@fullcalendar/google-calendar@6.1.19/index.global.min.js"></script>

<script>
  // tiny helper: grab the first URL (preferring Zoom) from the description
  function extractJoinLink(desc = "") {
    const text = String(desc);
    // prefer Zoom
    const zoomMatch = text.match(/https?:\/\/[\w.-]*zoom\.us\/[^\s)]+/i);
    if (zoomMatch) return zoomMatch[0];
    // otherwise first URL
    const any = text.match(/https?:\/\/\S+/i);
    return any ? any[0] : null;
  }

  document.addEventListener('DOMContentLoaded', () => {
    const cal = new FullCalendar.Calendar(document.getElementById('calendar'), {
      initialView: 'timeGridWeek',
      timeZone: 'America/Los_Angeles',
      nowIndicator: true,
      headerToolbar: { left: 'prev,next today', center: 'title', right: 'dayGridMonth,timeGridWeek,listWeek' },

      googleCalendarApiKey: 'AIzaSyDQ_G2do9l4G8ngIuOh3_mIg9bPWzcEb50',
      events: { googleCalendarId: '710ed87ef69dc6c9cb5ab690c7a2b802161c7d9e471e61375276c6d0173dc5ff@group.calendar.google.com' },

      // show location + a clean "Zoom link" / "Event link" line inside each event
      eventContent: (arg) => {
        const title = document.createElement('div');
        title.className = 'fc-event-title';
        title.textContent = arg.event.title || '(no title)';

        const loc = arg.event.extendedProps?.location?.trim();
        const desc = arg.event.extendedProps?.description || '';
        const link = extractJoinLink(desc);

        const meta = document.createElement('div');
        meta.className = 'fc-event-meta';
        if (loc) {
          const s = document.createElement('span');
          s.textContent = loc;
          meta.appendChild(s);
        }
        if (loc && link) {
          const dot = document.createElement('span');
          dot.textContent = ' • ';
          meta.appendChild(dot);
        }
        if (link) {
          const a = document.createElement('a');
          a.href = link;
          a.target = '_blank';
          a.rel = 'noopener noreferrer';
          a.textContent = /zoom\.us/i.test(link) ? 'Zoom link' : 'Event link';
          meta.appendChild(a);
        }

        return meta.childNodes.length ? { domNodes: [title, meta] } : { domNodes: [title] };
      },

      // add a tooltip with full description (plain text) on hover
      eventDidMount: (info) => {
        const d = (info.event.extendedProps?.description || '')
          .replace(/<[^>]+>/g, ' ')  // strip HTML just in case
          .replace(/\s+/g, ' ')
          .trim();
        if (d) info.el.title = d;
      },

      // intercept clicks: open Zoom/event link if present; otherwise do nothing
      eventClick: (info) => {
        const desc = info.event.extendedProps?.description || '';
        const link = extractJoinLink(desc);
        if (link) {
          info.jsEvent.preventDefault();
          window.open(link, '_blank', 'noopener,noreferrer');
        } else {
          // prevent navigating to Google event (students may not have accounts)
          info.jsEvent.preventDefault();
        }
      }
    });

    cal.render();
  });
</script>

<style>
  .fc .fc-event-title, .fc .fc-event-meta { white-space: normal; line-height: 1.2; }
  .fc .fc-event-meta { font-size: 0.85em; opacity: 0.9; margin-top: 2px; }
  .fc .fc-event-meta a { text-decoration: underline; }
</style>

</div>