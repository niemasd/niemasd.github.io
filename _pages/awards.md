---
layout: archive
title: "Awards"
permalink: /awards/
author_profile: true
---

<center><a href="#funding">Funding</a> – <a href="#honors-awards">Honors/Awards</a> – <a href="#conference-awards">Conference Awards</a></center>

{% include base_path %}

<h2 id="funding">Funding</h2>
<ul>{% for post in site.awards reversed %}
  {% if post.awardtype == 'funding' %}
    <li>
      <a href="{{ post.awardurl }}" target="_blank"><b>{{ post.awarder }}</b></a>
      <ul>
        <li><u>Amount</u>: {{ post.amount }}
        <li><u>Start Date</u>: {{ post.startdate }}</li>
        <li><u>End Date</u>: {{ post.enddate }}</li>
        <li><u>Title</u>: {{ post.title }}</li>
      </ul>
    </li>
  {% endif %}
{% endfor %}</ul>

<center>— <a href="#top">Top</a> —</center>

<h2 id="honors-awards">Honors/Awards</h2>
<ul>{% for post in site.awards reversed %}
  {% if post.awardtype == 'honor' %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}</ul>

<center>— <a href="#top">Top</a> —</center>

<h2 id="conference-awards">Conference Awards</h2>
<ul>{% for post in site.awards reversed %}
  {% if post.awardtype == 'conference' %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}</ul>

<center>— <a href="#top">Top</a> —</center>
