from flask import Flask

myobj = Flask(__name__)

@myapp_obj.route("/")
def home():
	name = "Lisa"
	city_names = ['Paris', 'London', 'Rome', 'Tahiti']
	return '''
	<html>
	<body>
		<h1>Welcome ''' + name + ''' </h1>
		<a href="https://www.google.com/"> not google</a>
		<p>
		<ul>
			<li> ''' + city_names[0] + ''' </li>
			<li> ''' + city_names[1] + ''' </li>
			<li> ''' + city_names[2] + ''' </li>
			<li> ''' + city_names[3] + ''' </li>
		</ul>
		</p>
	</body>
	</html>'''

# myapp_obj.run()
