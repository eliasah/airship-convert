{% block imports %}{% endblock %}
object SimpleApp {
  def main(args: Array[String]) {
    {% block init %}{% endblock %}
    {% for paragraph in paragraphs %}
    {{ paragraph.text | safe | indent(4) }}
    {% endfor %}
    {% block finalize %}{% endblock %}
  }
}