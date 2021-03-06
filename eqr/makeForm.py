import os
def makeForm(s):
    path='var/www/html/faithinnothing.me/eqr/eqr/templates/form.html'
    htmlStr = str(s.decode('utf-8')).replace("\\n", "<br>") #s is unfortunately encoded, decode?
    #htmlStr = s.replace("\\n", "<br>")
    base = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-16">
    <link type="text/css" rel="stylesheet" href="{{ url_for('static', filename='css/materialize.css') }}" media="screen,projection"/>
    <link type="text/css" rel="stylesheet" href="{{ url_for('static', filename='css/overlay.css') }}"/>
	<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
	<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
	<script type="text/javascript" src="{{ url_for('static', filename='js/materialize.js') }}"></script>
	<script type="text/javascript" src="{{ url_for('static', filename='js/init.js') }}"></script>
    <script type="text/javascript" src="{{ url_for('static', filename='js/input.js') }}"></script>
	<meta name="theme-color" content="#444d8b"> <!-- changed from #607d8b-->
    <title>Circuit Generator</title>
    <script>

    </script>
</head>

<body>
    <nav class="" role="navigation">
       <div class="nav-wrapper container"><a id="logo-container" href="/" class="brand-logo center">Approximate An Equivalent Resistance/Capacitance With Given Components</a>
       </div>
    </nav>
<pre>
%s
<br>
<br>
An example of how series/parallel components are being used here:
<br>
With parallel==0 and series == 1, a node layout of [1,0,1] means EQR == R0 + (R1 || (R2 + R3)),
e.g. R2 and R3 are in series, which is collectively in parallel with R1, the whole group of which
is in series with R0.
</pre>
</body>
</html>
""" % htmlStr
    #print(base)
    form = open(path,'w')
    form.write(base)
    form.close()
    return base
