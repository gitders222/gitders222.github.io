from flask import Flask, render_template, request
import pickle
#app = Flask('stock_pricer')

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))  # loading the model

@app.route('/')
def home():
    return render_template('Sverre Torp.html')
  

@app.route('/misc')
def misc():
    return render_template('misc.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/random')
def random():
    return render_template('random.html')

@app.route('/misc/misc1')
def misc1():
    return render_template('misc/misc1.html')


@app.route('/personal')
def personal():
    return render_template('personal.html')


@app.route('/predict',methods=['POST'])
def predict():
    """Grabs the input values and uses them to make prediction"""
    rooms = int(request.form["rooms"])
    distance = int(request.form["distance"])
    prediction = model.predict([[rooms, distance]])  # this returns a list e.g. [127.20488798], so pick first element [0]
    output = round(prediction[0], 2)

    return render_template('ai.html', prediction_text=f'A house with {rooms} rooms and located {distance} meters from the city center has a value of ${output}')


if __name__ == "__main__":
    app.run()


#@app.route('/')
#def show_predict_stock_form():
#	return render_template('predictorform.html')

#@app.route('/results', methods=['POST'])
#def results():
#	form = request.form
#	if request.method == 'POST':
#		#write your function that loads the model
#		model = get_model() #you can use pickle to load the trained model
#		year = request.form['year']
#		predicted_stock_price = model.predict(year)
#		return render_template('resultsform.html', year=year,   predicted_price=predicted_stock_price)

#app.run("localhost", "9999", debug=True)
