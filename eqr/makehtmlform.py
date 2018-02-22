import os
def makeform(s):
    path='/var/www/html/faithinnothing.me/cornertext/cornertext/templates/form.html'
    starter="""<!DOCTYPE html>
<html>
  <head>
    <title>Flask app</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
  </head>
  <body>
    <header>
      <div class="container">
        <h1 class="logo">CornerText</h1>
        <strong><nav>
        </nav></strong>
      </div>
    </header>
    <div class="container">
      {% block content %}
      {% endblock %}
    </div>
  </body>"""
    starter+="<pre>"+s+"""<div id="window-resizer-tooltip"><a href="#" title="Edit settings"></a><span class="tooltipTitle">Window size: </span><span class="tooltipWidth" id="winWidth"></span> x <span class="tooltipHeight" id="winHeight"></span><br><span class="tooltipTitle">Viewport size: </span><span class="tooltipWidth" id="vpWidth"></span> x <span class="tooltipHeight" id="vpHeight"></span></div>"""+"</pre"+"</html>"
    with open(path, "w"):
            pass
    form = open(path,'w')
    form.write(starter)
    return None
