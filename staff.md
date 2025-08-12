---
layout: default
title: Staff
permalink: /staff/
---

# Staff

{% assign roles = "Instructor|instructor,Course Coordinator|coordinator,Head Course Assistant|head_ca" | split: "," %}
{% for pair in roles %}
  {% assign parts = pair | split: "|" %}
  <h2>{{ parts[0] }}</h2>
  <div class="row row-cols-2 row-cols-sm-3 row-cols-md-4 row-cols-lg-5 g-4">
    {% for p in site.data.staff[parts[1]] %}
    <div class="col">
      <div class="text-center">
        <img src="{{ p.photo | relative_url }}"
             class="rounded-circle d-block mx-auto img-fluid"
             style="width:140px;height:140px;object-fit:cover;"
             alt="{{ p.name }}">
        <div class="mt-2 fw-semibold">
          {% if p.link %}<a href="{{ p.link }}" target="_blank" rel="noopener">{{ p.name }}</a>{% else %}{{ p.name }}{% endif %}
        </div>
        <div class="text-muted small">{{ parts[0] }}</div>
      </div>
    </div>
    {% endfor %}
  </div>
{% endfor %}

<h2>Course Assistants</h2>
<div class="row row-cols-2 row-cols-sm-3 row-cols-md-4 row-cols-lg-5 g-4">
  {% for p in site.data.staff.cas %}
  <div class="col">
    <div class="text-center">
      <img src="{{ p.photo | relative_url }}"
           class="rounded-circle d-block mx-auto img-fluid"
           style="width:120px;height:120px;object-fit:cover;"
           alt="{{ p.name }}">
      <div class="mt-2">{{ p.name }}</div>
    </div>
  </div>
  {% endfor %}
</div>
