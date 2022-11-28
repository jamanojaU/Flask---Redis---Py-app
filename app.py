from flask import Flask, render_template, request
import time
import redis

# Connect to Redis
r = redis.Redis(host = "redis", port=6379, db=0)

# Create Flask app
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_measure')
def new_measure():
    # Get the measure from the URL parameter
    return render_template('new_measure.html')

#This method is called when the user clicks on the button
@app.route('/new_measure', methods=['POST'])
def new_measure_id():
    if request.method == 'POST':
        measure = request.form.get('value')
        # Store the measure in Redis
        measure = measure + " --- " + str(time.time())
        r.rpush("measure", measure)
        return render_template('new_measure.html')
    else:
        return render_template('new_measure.html')

#This function shows all the measures
@app.route('/show_measure')
def show_measure():
    list = []
    #Check is the list is empty
    if r.llen("measure") == 0:
        return render_template('show_measure.html', measures=list)
    for i in range(0, r.llen("measure")):
        list.append(r.lindex("measure", i))
    return render_template('show_measure.html', measures=list)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)