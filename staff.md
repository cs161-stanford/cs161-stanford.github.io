---
layout: default
title: Staff
permalink: /staff/
---

# Staff

<h4>Instructor</h4>
<div class="row row-cols-2 row-cols-sm-3 row-cols-md-4 row-cols-lg-5 g-4">
  {% for p in site.data.staff.instructor %}
  <div class="col">
    <div class="text-center">
      <img src="{{ p.photo | relative_url }}"
           class="rounded-circle d-block mx-auto img-fluid"
           style="width:160px;height:160px;object-fit:cover;"
           alt="{{ p.name }}">
      <div class="mt-2 fw-semibold">
        {% if p.link %}<a href="{{ p.link }}" target="_blank" rel="noopener">{{ p.name }}</a>{% else %}{{ p.name }}{% endif %}
      </div>
      <div class="text-muted small">Favorite Algorithm: {{p.algorithm}}</div>
    </div>
  </div>
  {% endfor %}
</div>

<h4>Course Coordinator</h4>
<div class="row row-cols-2 row-cols-sm-3 row-cols-md-4 row-cols-lg-5 g-4">
  {% for p in site.data.staff.coordinator %}
  <div class="col">
    <div class="text-center">
      <img src="{{ p.photo | relative_url }}"
           class="rounded-circle d-block mx-auto img-fluid"
           style="width:140px;height:140px;object-fit:cover;"
           alt="{{ p.name }}">
      <div class="mt-2 fw-semibold">
        {% if p.link %}<a href="{{ p.link }}" target="_blank" rel="noopener">{{ p.name }}</a>{% else %}{{ p.name }}{% endif %}
      </div>
      <div class="text-muted small">Favorite Algorithm: {{p.algorithm}}</div>
    </div>
  </div>
  {% endfor %}
</div>

<h4>Head Course Assistant</h4>
<div class="row row-cols-2 row-cols-sm-3 row-cols-md-4 row-cols-lg-5 g-4">
  {% for p in site.data.staff.head_ca %}
  <div class="col">
    <div class="text-center">
      <img src="{{ p.photo | relative_url }}"
           class="rounded-circle d-block mx-auto img-fluid"
           style="width:140px;height:140px;object-fit:cover;"
           alt="{{ p.name }}">
      <div class="mt-2 fw-semibold">{{ p.name }}</div>
      <div class="text-muted small">Favorite Algorithm: {{p.algorithm}}</div>
    </div>
  </div>
  {% endfor %}
</div>

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
      <div class="text-muted small">Favorite Algorithm: {{p.algorithm}}</div>
    </div>
  </div>
  {% endfor %}
</div>
