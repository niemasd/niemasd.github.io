---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Academic Positions
======
* **2019–Present — Assistant Teaching Professor**
  * [Computer Science & Engineering](https://cse.ucsd.edu/)
  * [University of California, San Diego](https://ucsd.edu/)

Education
======
* **2015–2019 — Ph.D. in Bioinformatics and Systems Biology**
  * [University of California, San Diego](https://ucsd.edu/)
* **2011–2015 — B.S. in Bioengineering: Bioinformatics**
  * Minor in Economics
  * [University of California, San Diego](https://ucsd.edu/)

Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
