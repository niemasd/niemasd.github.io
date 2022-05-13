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
      <a href="{{ post.awardurl }}" target="_blank"><b>{{ post.awarder }} ({{ post.amount }})</b></a>
      <ul>
        <p class="archive__item-excerpt" itemprop="description"><li><u>Duration</u>: {{ post.startdate }} to {{ post.enddate }}</li></p>
        <p class="archive__item-excerpt" itemprop="description"><li><u>Title</u>: {{ post.title }}</li></p>
        <p class="archive__item-excerpt" itemprop="description"><li><u>Team</u>: {{ post.team }}</li></p>
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
