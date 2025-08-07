---
layout: default
title: Policies
permalink: /policies/
---

# Policies

{% assign pols = "Collaboration Policy,LLM Policy,Honor Code,Regrade Policy,Late Homework and Missed Exam Policy,Course Grade Policy,Bonus Point Policy,Bug Bounty Policy" | split: "," %}
{% for p in pols %}
<div class="panel policy-panel">
  <h2>{{ p }}</h2>
  <!-- Policy text here -->
</div>
{% endfor %}
