---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<center><a href="#textbooks">Textbooks</a> – <a href="#papers-articles">Papers/Articles</a> – <a href="#conference-presentations">Conference Presentations</a></center>

{% include base_path %}

<h2 id="textbooks">Textbooks</h2>
<ol reversed>{% for post in site.publications reversed %}
  {% if post.pubtype == 'textbook' %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}</ol>

<h2 id="papers-articles">Papers/Articles</h2>
<ol reversed>{% for post in site.publications reversed %}
  {% if post.pubtype == 'paper' %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}</ol>

<h2 id="conference-presentations">Conference Presentations</h2>
<ol reversed>{% for post in site.publications reversed %}
  {% if post.pubtype == 'conference' %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}</ol>
