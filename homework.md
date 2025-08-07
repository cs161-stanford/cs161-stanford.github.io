---
layout: default
title: Homework
permalink: /homework/
---

# Homework

{% for h in (1..7) %}
<div class="panel homework-panel">
  <h2>Homework {{ h }}</h2>
  <p><strong>Release Date:</strong> <!-- YYYY-MM-DD --></p>
  <p><strong>Due Date:</strong> <!-- YYYY-MM-DD --></p>
  <p>
    <a href="#">Problem Set (PDF)</a> |
    <a href="#">LaTeX Template</a>
  </p>
</div>
{% endfor %}
