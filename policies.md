---
layout: default
title: Policies
permalink: /policies/
---

# Policies

 <div class="card mb-3">
    <div class="card-header">
      <button class="btn btn-link text-decoration-none"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#cardOne"
              aria-expanded="false"
              aria-controls="cardOne">
        Collaboration Policy
      </button>
    </div>
    <div id="cardOne" class="collapse">
      <div class="card-body">

Here is the Collaboration Policy for Homework and Exams. Please check with the course staff if you have questions about what is or is not permitted.
<ul><li>
The HW assignments will be submitted in small groups (up to three). It is fine and good to discuss between groups (please acknowledge your collaborators), but each group must type up their solutions on their own, from scratch.</li>
<ul><li>
The following is OK: Your group and another group work through the problems together over a couple of days. You bounce ideas off each other, and eventually come up with a pretty good solution idea. You and your group type up that idea in your own words, perhaps lightly consulting notes you took while working with the other group.</li>
<li>The following is NOT OK: Your group and another group work through the problems together over a couple of days. You bounce ideas off each other, and eventually come up with a pretty good solution idea. Your group types up the solutions first. Since the other group helped, you share your write-up with them as a starting point for their own write-up.<li>
<li>A good test: if you ever share your typed-up solutions with another group, or if someone shares theirs with you, it is probably NOT OKAY.
Collaboration outside of this quarter's CS161 class is not allowed.</li></ul>
</li>
<li>
No collaboration is permitted on exams.      
</li></ul>

</div>
    </div>
  </div>

{% assign pols = "Collaboration Policy,LLM Policy,Honor Code,Regrade Policy,Late Homework and Missed Exam Policy,Course Grade Policy,Bonus Point Policy,Bug Bounty Policy" | split: "," %}
{% for p in pols %}
<div class="panel policy-panel">
  <h2>{{ p }}</h2>
  <!-- Policy text here -->
</div>
{% endfor %}
