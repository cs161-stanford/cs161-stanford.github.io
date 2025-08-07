---
layout: default
title: Exams
permalink: /exams/
---

# Exams

{% for e in (1..3) %}
<!--<div class="panel exam-panel">-->
<div class="card">
  <h2>Exam {{ e }}</h2>
  <p><strong>Date:</strong> <!-- YYYY-MM-DD --></p>
  <p><a href="#">Exam PDF</a></p>
</div>
{% endfor %}
