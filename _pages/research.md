---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

<center><a href="#papers-articles">Papers/Articles</a> – <a href="#conference-presentations">Conference Presentations</a> – <a href="#preprints-reports">Preprints/Reports</a></center>

<p style="font-size:0.9em">You can find a complete list of my collaborators in this <a href="https://docs.google.com/spreadsheets/d/1rLfHiTx6qOnTN3czttHOL6JIAhptFAfodojjY8D2gqg/edit?usp=sharing" target="_blank">Google Sheet</a>.</p>

{% include base_path %}

<h2 id="papers-articles">Papers/Articles</h2>
<ol reversed>{% for post in site.publications reversed %}
  {% if post.pubtype == 'paper' %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}</ol>

<center>— <a href="#top">Top</a> —</center>

<h2 id="conference-presentations">Conference Presentations</h2>
<ol reversed>{% for post in site.publications reversed %}
  {% if post.pubtype == 'conference' %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}</ol>

<center>— <a href="#top">Top</a> —</center>

<h2 id="preprints-reports">Preprints/Reports</h2>
<ol reversed>{% for post in site.publications reversed %}
  {% if post.pubtype == 'preprint' %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}</ol>

<center>— <a href="#top">Top</a> —</center>
