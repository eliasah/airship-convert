{% block imports %}{% endblock %}
object SimpleApp {
  def main(args: Array[String]) {
    {% block init %}{% endblock %}
    {% for paragraph in paragraphs %}
    {{ paragraph.text | safe }}
    {% endfor %}
    {% block finalize %}{% endblock %}
  }
}