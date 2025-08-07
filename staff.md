---
layout: default
title: Staff
permalink: /staff/
---

# Staff

<div class="panel">
  <h2>Instructor</h2>
  <img src="/assets/img/mary.jpg" alt="Mary Wootters">
  <p><a href="https://sites.google.com/site/marywootters">Mary Wootters</a></p>
</div>

<div class="panel">
  <h2>Course Coordinator</h2>
  <img src="/assets/img/amelie.jpg" alt="Amelie Byun">
  <p><a href="#">Amelie Byun</a></p>
</div>

<div class="panel">
  <h2>Head Course Assistant</h2>
  <img src="/assets/img/placeholder.jpg" alt="Head CA">
  <p>Name</p>
</div>

<div class="panel">
  <h2>Course Assistants</h2>
  {% for i in (1..15) %}
  <div class="assistant">
    <img src="/assets/img/placeholder.jpg" alt="CA {{ i }}">
    <p>Name {{ i }}</p>
  </div>
  {% endfor %}
</div>
