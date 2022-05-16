---
layout: archive
title: "Students"
permalink: /students/
author_profile: true
---

{% include base_path %}

{% assign presentyear = 'now' | date: "%Y" }

{% assign endyears = '' %}
{% for student in site.students %}
  {% assign endyears = endyears | append: ' ' | append: student.endyear %}
{% endfor %}
{% assign endyears = endyears | lstrip | split: ' ' | uniq | sort %}

{% for endyear in endyears reversed %}
  {% if endyear == "Present" %}
    {% continue %}
  {% endif %}
  <h2 id="{{ endyear }}">{{ endyear }}</h2>
  <ul>{% for student in site.students %}
    {% if student.endyear == 'Present' %}
      {% assign student_endyear = presentyear %}
    {% else %}
      {% assign student_endyear = student.endyear %}
    {% endif %}
    {% if student_endyear != endyear %}
      {% continue %}
    {% endif %}
    {% assign tmp = '<b>' | append: student.firstname | append: ' ' | append: student.lastname | append: '</b>' %}
    {% if student.website %}
      {% assign tmp = '<a href="' | append: student.website | append: '" target="_blank">' | append: tmp | append: '</a>' %}
    {% endif %}
    {% assign tmp = tmp | append: ' — ' | append: student.role %}
    {% if student.advisor %}
      {% assign tmp2 = student.advisor %}
      {% if student.advisorwebsite %}
        {% assign tmp2 = '<a href="' | append: student.advisorwebsite | append: '" target="_blank">' | append: tmp2 | append: '</a>' %}
      {% endif %}
      {% assign tmp = tmp | append: ' (Advisor: ' | append: tmp2 | append: ')' %}
    {% endif %}
    <li>{{ tmp }}</li>
  {% endfor %}</ul>
{% endfor %}

<center><b>TODO: REMOVE EVERYTHING BELOW</b></center>

<h2 id="funding">Funding</h2>
<ul>{% for post in site.awards reversed %}
  {% if post.awardtype == 'funding' %}
    <li>
      <a href="{{ post.awardurl }}" target="_blank"><b>{{ post.awarder }} ({{ post.amount }})</b></a>
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
