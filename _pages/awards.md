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
      <a style="text-decoration:underline" href="{{ post.awardurl }}" target="_blank"><b>{{ post.awarder }} ({{ post.amount }})</b></a>
      <ul style="font-size:0.75em">
        <li><u>Duration</u>: {{ post.startdate }} to {{ post.enddate }}</li>
        <li><u>Title</u>: {{ post.title }}</li>
        <li><u>Team</u>: {{ post.team }}</li>
      </ul>
    </li>
  {% endif %}
{% endfor %}</ul>

<center>— <a href="#top">Top</a> —</center>

<h2 id="honors-awards">Honors/Awards</h2>
<ul>{% for post in site.awards reversed %}
  {% if post.awardtype == 'honor' %}
    <li>
      <a href="{{ post.awardurl }}" target="_blank"><b>{{ post.title }}</b></a>
      <ul style="font-size:0.75em">
        <li><u>Award Date</u>: {{ post.startdate }}</li>
        <li><u>Awarder</u>: {{ post.awarder }}</li>
        {% if post.videourl %}
          <li><u>Video</u>: <a href="{{ post.videourl }}" target="_blank">{{ post.videourl }}</a></li>
        {% endif %}
      </ul>
    </li>
  {% endif %}
{% endfor %}</ul>

<center>— <a href="#top">Top</a> —</center>

<h2 id="conference-awards">Conference Awards</h2>
<ul>{% for post in site.awards reversed %}
  {% if post.awardtype == 'conference' %}
    <li>
      <a href="{{ post.awardurl }}" target="_blank"><b>{{ post.title }}</b></a>
      <ul style="font-size:0.75em">
        <li><u>Award Date</u>: {{ post.startdate }}</li>
        <li><u>Awarder</u>: {{ post.awarder }}</li>
        {% if post.videourl %}
          <li><u>Video</u>: <a href="{{ post.videourl }}" target="_blank">{{ post.videourl }}</a></li>
        {% endif %}
      </ul>
    </li>
  {% endif %}
{% endfor %}</ul>

<center>— <a href="#top">Top</a> —</center>
