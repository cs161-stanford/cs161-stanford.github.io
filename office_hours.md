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
  document.addEventListener('DOMContentLoaded', () => {
    const cal = new FullCalendar.Calendar(document.getElementById('calendar'), {
      initialView: 'timeGridWeek', // start on weekly view
      timeZone: 'America/Los_Angeles',
      nowIndicator: true,

      // add view-switch buttons on the right
      headerToolbar: {
        left: 'prev,next today',
        center: 'title',
        right: 'dayGridMonth,timeGridWeek,listWeek'
      },

      // (optional) make it taller
      contentHeight: 700,

      googleCalendarApiKey: 'AIzaSyDQ_G2do9l4G8ngIuOh3_mIg9bPWzcEb50',
      events: { googleCalendarId: '710ed87ef69dc6c9cb5ab690c7a2b802161c7d9e471e61375276c6d0173dc5ff@group.calendar.google.com' }
    });
    cal.render();
  });
</script>

</div>