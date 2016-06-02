{% extends "python/base.pyi" %}
{% block imports %}
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
{% endblock %}
{% block init %}
    conf = SparkConf().setAppName("{{ id }}")
    sc = SparkContext(conf=conf)
{% endblock init %}
{% block finalize %}
    sc.stop()
{% endblock %}
