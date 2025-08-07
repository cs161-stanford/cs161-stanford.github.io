---
layout: default
title: Lectures
permalink: /lectures/
---

# Lectures

<div class="card mb-4">
  <div class="card-header">
    Lecture 1: Why are you here?
  </div>
  <div class="card-body">
    <p class="card-text">
    <h5 class="card-title">Before Class</h5>
	<ul>
	<li> Nothing, it's the first class! </li>
	</ul>
    <h5 class="card-title">During Class</h5>
	<ul>
	<li> <a href="assets/lectures/lecture1.pptx">Slides (pptx)</a> </li>
	<li> <a href="assets/lectures/lecture1.pdf">Slides (pdf)</a> </li>
	<li> <a href="assets/notebooks/lecture1.ipynb">IPython Notebook: Karatsuba's Algorithm</a>
	<li> <a href="assets/notebooks/lecture1_aux.py">auxiliary .py file for IPython Notebook</a>
	</ul>
<h5 class="card-title">Relevant Reading</h5>
<ul><li>
AI Chapter 1
</ul>

  </div>
</div>


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
