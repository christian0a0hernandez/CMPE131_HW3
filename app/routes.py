from app import myobj
from flask import render_template, flash, request, redirect, url_for

@myobj.route("/", methods=['GET', 'POST'])
def home():
	name = "Lisa"
	city_names = ['Paris', 'London', 'Rome', 'Tahiti']
	new_city = ""
	if (request.method == 'POST'):
		new_city = request.form['cityName']
		flash(new_city)
		return redirect(url_for('home'))
	return render_template('home.html',cities=city_names,username=name)

if __name__ == "__main__":
	app.run(port=80)
