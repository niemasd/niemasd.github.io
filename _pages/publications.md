---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<section id="top">
<center><a href="#textbooks">Textbooks</a> – <a href="#papers-articles">Papers/Articles</a> – <a href="#conference-presentations">Conference Presentations</a> – <a href="#preprints">Preprints</a></center>
</section>

{% include base_path %}

<h2 id="textbooks">Textbooks</h2>
<ol reversed>{% for post in site.publications reversed %}
  {% if post.pubtype == 'textbook' %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}</ol>

<center>— <a href="#top">Top</a> —</center>

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

<h2 id="preprints">Preprints</h2>
<ol reversed>{% for post in site.publications reversed %}
  {% if post.pubtype == 'preprint' %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}</ol>

<center>— <a href="#top">Top</a> —</center>
