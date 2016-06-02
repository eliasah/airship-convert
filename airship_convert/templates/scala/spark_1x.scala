{% extends "scala/base.scala" %}
{% block imports %}
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf
import org.apache.spark.sql.SQLContext
{% endblock %}
{% block init %}
    val conf = new SparkConf().setAppName("{{ id }}")
    val sc = new SparkContext(conf)
    val sqlContext = new SQLContext(sc)
{% endblock %}

{% block finalize %}
    sc.stop()
{% endblock %}
