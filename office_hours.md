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
  <link href="https://cdn.jsdelivr.net/npm/fullcalendar@6.1.15/main.min.css" rel="stylesheet">
  <div id="calendar" style="max-width:1100px;margin:20px auto;"></div>
  <script src="https://cdn.jsdelivr.net/npm/fullcalendar@6.1.15/index.global.min.js"></script>

  <script>
  // grab first URL from description (handles raw URL or <a href=...>)
  function extractFirstUrl(desc = "") {
    // 1) if there’s an <a href="...">, grab href
    const hrefMatch = desc.match(/href="([^"]+)"/i);
    let url = hrefMatch ? hrefMatch[1] : null;

    // 2) otherwise, match plain https://... text
    if (!url) {
      const plain = desc.match(/https?:\/\/\S+/i);
      url = plain ? plain[0] : null;
    }
    if (!url) return null;

    // Unwrap Google's redirect links: https://www.google.com/url?q=ACTUAL&...
    try {
      const u = new URL(url);
      if (u.hostname.includes('google.com') && u.searchParams.get('q')) {
        url = u.searchParams.get('q');
      }
    } catch {}
    return url;
  }

  document.addEventListener('DOMContentLoaded', () => {
    const calendar = new FullCalendar.Calendar(document.getElementById('calendar'), {
      initialView: 'timeGridWeek',
      timeZone: 'America/Los_Angeles',
      nowIndicator: true,
      headerToolbar: { left: 'prev,next today', center: 'title', right: 'dayGridMonth,timeGridWeek,listWeek' },
      events: '{{ "/assets/calendar/events.json" | relative_url }}?v={{ site.time | date: "%s" }}',

      eventContent: (arg) => {
        const title = document.createElement('div');
        title.className = 'fc-event-title';
        title.textContent = arg.event.title;

        const loc = arg.event.extendedProps?.location?.trim();
        const desc = arg.event.extendedProps?.description || "";
        const url  = extractFirstUrl(desc);

        // build a clean meta line: "Huang Basement • Zoom link"
        const meta = document.createElement('div');
        meta.className = 'fc-event-meta';

        if (loc) {
          const locSpan = document.createElement('span');
          locSpan.textContent = loc;
          meta.appendChild(locSpan);
        }
        if (loc && url) {
          const sep = document.createElement('span');
          sep.textContent = ' • ';
          meta.appendChild(sep);
        }
        if (url) {
          const a = document.createElement('a');
          a.href = url;
          a.target = '_blank';
          a.rel = 'noopener noreferrer';
          // label smartly based on domain
          a.textContent = /zoom\.us|stanford\.zoom\.us/i.test(url) ? 'Zoom link' : 'Event link';
          meta.appendChild(a);
        }

        // If neither loc nor url, show nothing extra
        return meta.childNodes.length ? { domNodes: [title, meta] } : { domNodes: [title] };
      },

      // optional: tooltip with full description (as plain text)
      eventDidMount: (info) => {
        const d = (info.event.extendedProps?.description || '')
          .replace(/<[^>]+>/g, ' ')    // strip tags
          .replace(/\s+/g, ' ')        // collapse whitespace
          .trim();
        if (d) info.el.title = d;
      }
    });
    calendar.render();
  });
</script>

<style>
.fc .fc-event-title, .fc .fc-event-meta { white-space: normal; line-height: 1.2; }
.fc .fc-event-meta { font-size: 0.85em; opacity: 0.9; margin-top: 2px; }
.fc .fc-event-meta a { text-decoration: underline; }
</style>


<style>
/* allow wrapping so long text doesn't get cut off */
.fc .fc-event-title, .fc .fc-event-meta { white-space: normal; line-height: 1.2; }
.fc .fc-event-meta { font-size: 0.85em; opacity: 0.85; margin-top: 2px; }
</style>

</div>
