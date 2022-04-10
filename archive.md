---
layout: page
title: archive
---

{% for tag in site.tags %}
  <h3>{{ tag[0] }}</h3>
  <ul>
    {% for post in tag[1] %}
      <li>{{ post.date | date: "%B %Y" }} - <a href="{{ post.url }}" class= "{{ tag[0] }}" > {{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}
