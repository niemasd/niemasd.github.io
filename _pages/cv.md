---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<center><a href="#academic-positions">Academic Positions</a> – <a href="#education">Education</a> – <a href="#institutional-service">Institutional Service</a> – <a href="#reviewer">Reviewer</a></center>

<p style="font-size:0.9em">You can download a PDF of my CV <a href="https://github.com/niemasd/curriculum-vitae/releases/latest/download/main.pdf" target="_blank">here</a>. You can find my academic positions and education history below, and you can find all other information via the links above (e.g. "Awards", "Publications", etc.).</p>

<h2 id="academic-positions">Academic Positions</h2>
<ul>
  <li><b><u>Assistant Teaching Professor (2019–Present)</u></b></li>
  <ul style="font-size:0.75em">
    <li><a href="https://cse.ucsd.edu/" target="_blank">Computer Science & Engineering</a></li>
    <li><a href="https://ucsd.edu/" target="_blank">University of California, San Diego</a></li>
  </ul>
</ul>

<center>— <a href="#top">Top</a> —</center>

<h2 id="education">Education</h2>
<ul>
  <li><b><u>Ph.D. in Bioinformatics and Systems Biology (2015–2019)</u></b></li>
  <ul style="font-size:0.75em">
    <li><a href="https://ucsd.edu/" target="_blank">University of California, San Diego</a></li>
    <li>Co-advised by <a href="http://eceweb.ucsd.edu/~smirarab/" target="_blank">Siavash Mirarab</a> and <a href="https://bioalgorithms.ucsd.edu/" target="_blank">Pavel Pevzner</a></li>
  </ul>
  <li><b><u>B.S. in Bioengineering: Bioinformatics (2011–2015)</u></b></li>
  <ul style="font-size:0.75em">
    <li><a href="https://ucsd.edu/" target="_blank">University of California, San Diego</a></li>
    <li>Minor in <a href="https://economics.ucsd.edu/undergraduate-program/major-minor-requirements/minors.html" target="_blank">Economics</a></li>
  </ul>
</ul>

<center>— <a href="#top">Top</a> —</center>

<h2 id="institutional-service">Institutional Service</h2>
<ul>{% for post in site.service reversed %}
  {% if post.servicetype == 'institutional' %}
    <li>
      <b><u>{{ post.title }}</u></b>
      <ul style="font-size:0.75em">
        <li><u>Group</u>: {{ post.group }}</li>
        <li><u>Duration</u>: {{ post.startdate }} to {{ post.enddate }}</li>
      </ul>
    </li>
  {% endif %}
{% endfor %}</ul>

<center>— <a href="#top">Top</a> —</center>

<h2 id="reviewer">Reviewer</h2>
<ul>
  <li><b><u>Journal</u></b></li>
  <ul style="font-size:0.75em">{% for post in site.reviewer %}
    {% if post.reviewertype == 'journal' %}
      <li><a href="{{ post.venueurl }}" target="_blank">{{ post.title }}</a></li>
    {% endif %}
  {% endfor %}</ul>
  <li><b><u>Conference</u></b></li>
  <ul style="font-size:0.75em">{% for post in site.reviewer %}
    {% if post.reviewertype == 'conference' %}
      <li><a href="{{ post.venueurl }}" target="_blank">{{ post.title }}</a></li>
    {% endif %}
  {% endfor %}</ul>
</ul>

<center>— <a href="#top">Top</a> —</center>
