#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import
{% block imports %}{% endblock %}

def main():
    {% block init %}{% endblock init %}

    {% for paragraph in paragraphs %}
    {{ paragraph.text | safe | indent(4) }}
    {% endfor %}
    {% block finalize %}{% endblock %}

    pass


if __name__ == "__main__":
    main()
