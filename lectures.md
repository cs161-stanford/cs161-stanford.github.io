---
layout: default
title: Lectures
permalink: /lectures/
---

# Lectures

{% for i in (1..20) %}
<div class="panel lecture-panel">
  <h2>Lecture {{ i }}</h2>
  <p><strong>Date:</strong> <!-- YYYY-MM-DD --></p>
  <p><strong>Title:</strong> <!-- Lecture title --></p>
  <h3>Before Class</h3>
  <ul><li><!-- ... --></li></ul>
  <h3>During Class</h3>
  <ul><li><!-- ... --></li></ul>
  <h3>Relevant Reading</h3>
  <ul><li><!-- ... --></li></ul>
</div>
{% endfor %}
