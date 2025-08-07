---
layout: default
title: Resources
permalink: /resources/
---

# Resources

{% assign res = "Accommodations,Mental Health,Textbooks,Algorithmic Problem-Solving Resources,Concept Checks,Summation Formulae,Prerequisite Resources,LaTeX Resources,Homework Resources,SGOE Resources,Other Resources" | split: "," %}
{% for r in res %}
<div class="panel resource-panel">
  <h2>{{ r }}</h2>
  <!-- Add links/text here -->
</div>
{% endfor %}
