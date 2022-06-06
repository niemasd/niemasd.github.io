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

<center>
{% assign tmp = '' %}
{% for endyear in endyears reversed %}
  {% if endyear != "Present" %}
    {% if endyear != endyears.last %}
      {% assign tmp = tmp | append: ' – ' %}
    {% endif %}
    {% assign tmp = tmp | append: '<a href="#' | append: endyear | append: '">' | append: endyear | append: '</a>' %}
  {% endif %}
{% endfor %}
{{ tmp }}
</center>

<p style="font-size:0.9em">I have been <i>incredibly</i> fortunate to have gotten the opportunity to mentor amazing undergraduate and graduate students. A complete list of my past students can be found below.</p>

{% for endyear in endyears reversed %}
  {% if endyear == "Present" %}
    {% continue %}
  {% endif %}
  <h2 id="{{ endyear }}">{{ endyear }}</h2>
  <ul style="font-size:0.75em">{% for student in site.students %}
    {% if student.endyear == 'Present' %}
      {% assign tmpyear = presentyear %}
    {% else %}
      {% assign tmpyear = student.endyear %}
    {% endif %}
    {% if tmpyear != endyear %}
      {% continue %}
    {% endif %}
    {% assign tmp = '<b>' | append: student.firstname | append: ' ' | append: student.lastname | append: '</b>' %}
    {% if student.website %}
      {% assign tmp = '<a href="' | append: student.website | append: '" target="_blank">' | append: tmp | append: '</a>' %}
    {% endif %}
    {% assign tmp = tmp | append: ' — ' %}
    {% assign tmp2 = student.role %}
    {% if student.rolewebsite %}
      {% assign tmp2 = '<a href="' | append: student.rolewebsite | append: '" target="_blank">' | append: tmp2 | append: '</a>' %}
    {% endif %}
    {% assign tmp = tmp | append: tmp2 %}
    {% if student.advisor %}
      {% assign tmp2 = student.advisor %}
      {% if student.advisorwebsite %}
        {% assign tmp2 = '<a href="' | append: student.advisorwebsite | append: '" target="_blank">' | append: tmp2 | append: '</a>' %}
      {% endif %}
      {% assign tmp = tmp | append: ' (Advisor: ' | append: tmp2 | append: ')' %}
    {% endif %}
    {% assign tmp = tmp | append: ' (' | append: student.startyear %}
    {% if tmpyear != student.startyear %}
      {% assign tmp = tmp | append: '–' | append: tmpyear %}
    {% endif %}
    {% assign tmp = tmp | append: ')' %}
    <li>{{ tmp }}</li>
  {% endfor %}</ul>
  <center>— <a href="#top">Top</a> —</center>
{% endfor %}
