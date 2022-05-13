---
layout: archive
title: "Awards"
permalink: /awards/
author_profile: true
---

<center><a href="#funding">Funding</a> – <a href="#honors-awards">Honors/Awards</a> – <a href="#conference-awards">Conference Awards</a></center>

{% include base_path %}

<h2 id="funding">Funding</h2>
<ol reversed>{% for post in site.awards reversed %}
  {% if post.awardtype == 'funding' %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}</ol>

<center>— <a href="#top">Top</a> —</center>

<h2 id="honors-awards">Honors/Awards</h2>
<ol reversed>{% for post in site.awards reversed %}
  {% if post.awardtype == 'honor' %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}</ol>

<center>— <a href="#top">Top</a> —</center>

<h2 id="conference-awards">Conference Awards</h2>
<ol reversed>{% for post in site.awards reversed %}
  {% if post.awardtype == 'conference' %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}</ol>

<center>— <a href="#top">Top</a> —</center>
