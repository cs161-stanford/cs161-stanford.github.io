---
layout: default
title: Policies
permalink: /policies/
---

# Course Policies


<div class="card mb-3">
    <div class="card-header">
      <button class="btn btn-link text-decoration-none"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#grading"
              aria-expanded="false"
              aria-controls="grading">
        Grading Policy
      </button>
    </div>
    <div id="grading" class="collapse">
      <div class="card-body">
	The elements of your grade are:
	<ul>
		<li> 7 homework assignments (21%, or 3% each).
		<li> One "pre-HW assignment" (1%), graded for completion.
		<li> Exam I (Oct 16) (22%)
		<li> Exam II (Nov 6) (22%)
		<li> Final Exam (TBD) (34%)
                <li> Bonus Points (see Bonus Point Policy below).
	</ul>
      </div>
    </div>
  </div>


 <div class="card mb-3">
    <div class="card-header">
      <button class="btn btn-link text-decoration-none"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#collab"
              aria-expanded="false"
              aria-controls="collab">
        Collaboration Policy
      </button>
    </div>
    <div id="collab" class="collapse">
      <div class="card-body">
<ul>
<li>The HW assignments will be submitted in small groups (up to three). It is fine and good to discuss between groups (please acknowledge your collaborators), but each group must type up their solutions on their own, from scratch.
	<ul>
	<li>The following is OK: Your group and another group work through the problems together over a couple of days. You bounce ideas off each other, and eventually come up with a pretty good solution idea. You and your group type up that idea in your own words, perhaps lightly consulting notes you took while working with the other group.</li>
	<li>The following is NOT OK: Your group and another group work through the problems together over a couple of days. You bounce ideas off each other, and eventually come up with a pretty good solution idea. Your group types up the solutions first. Since the other group helped, you share your write-up with them as a starting point for their own write-up.</li>
	<li>A good test: if you ever share your typed-up solutions with another group, or if someone shares theirs with you, it is probably NOT OKAY.
Collaboration outside of this quarter's CS161 class is not allowed.</li>
	</ul>
</li>
<li>
No collaboration is permitted on exams.      
</li>
</ul>
Please check with the course staff if you have questions about what collaboration is or is not permitted.
</div>
</div>
</div>
 

<div class="card mb-3">
    <div class="card-header">
      <button class="btn btn-link text-decoration-none"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#llm"
              aria-expanded="false"
              aria-controls="llm">
        LLM Policy
      </button>
    </div>
    <div id="llm" class="collapse">
      <div class="card-body">
LLMs are a useful tool, but they can also be a crutch.  In this class, we want to encourage you to learn how to effectively use LLMs as a tool, while still giving you incentives to learn the material yourself.  
<ul><li> <i> Aside: Why should you learn the material yourself if LLMs can do lots of it? </i> LLMs currently can't do as well at algorithm design and analysis as skilled humans at the highest level, and Mary would argue that they won't in the near future (keeping in mind that humans get more powerful as our tools get more powerful).  If you want to eventually be an algorithmically-high-skilled human, you'll need to learn the basics so that you can surpass LLMs (possibly by using LLMs).  Also, in the short term, LLMs still make mistakes, and if you hand in buggy AI slop you'll get a bad grade.
</li></ul>
<br>
With that in mind, the policy is:
<ul>
<li> You are allowed to use LLMs for homework. <b>However,</b> we want you to be thoughtful about how you use them.  To that end:
<ul><li>Homework questions may even have a recommendation for how to use LLMs, for example "try to do this without LLMs," or "use an LLM to generate some ideas and refine them yourself," or "come up with some ideas yourself and use an LLM to refine them."  </li>
<li>These are only suggestions, and you can do what you think is best for your learning.</li>
</ul></li>
<li> You are <b>not</b> allowed to use LLMs on the exams.  It is a violation of the honor code to use LLMs, or any other resource other than your cheat-sheet, during the exams.
	<ul>
	<li>The exams are the incentive for you to follow our suggestions (or whatever you think is best for your <i>learning</i>) on the homework.</li>
	</ul></li>
</ul>
</div>
</div>
</div>
  
<div class="card mb-3">
    <div class="card-header">
      <button class="btn btn-link text-decoration-none"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#honor"
              aria-expanded="false"
              aria-controls="honor">
        Honor Code
      </button>
    </div>
    <div id="honor" class="collapse">
      <div class="card-body">
	More generally than the collaboration policy and LLM policy, we expect students to follow the <a href="https://communitystandards.stanford.edu/policies-guidance/honor-code">Stanford Honor Code</a>.  If we have reason to believe that you are in violation of the honor code, including violation of the Collaboration Policy or LLM Policy, we will follow University policy to report it to the Office of Community Standards.
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
