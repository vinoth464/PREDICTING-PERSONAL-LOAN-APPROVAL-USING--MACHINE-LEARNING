
import numpy as np
import pickle
import pandas
from flask import Flask, request, render_template

app = Flask(__name__)
model = pickle.load(open(r'model.pk1', 'rb'))
scale = pickle.load(open(r'scale.pk1', 'rb'))


@app.route('/')  # rendering the html template
def home():
    return render_template('index11.html')


@app.route('/predict', methods=["POST", "GET"])  # rendering the html template
def predict():
    return render_template('prediction_new.html')


@app.route('/submit', methods=["POST", "GET"])  # route to show the predictions in a web UI
def submit():
    # reading the inputs given by the user
    input_feature = [int(x) for x in request.form.values()]
    # input_feature = np.transpose(input_feature)
    Input_feature = [np.array(input_feature)]
    Print(input_feature)
    names = ['Gender', ‘Married’, ‘Dependents’, ‘Education’, ‘Self_Employed’, ‘, ApplicantIncome’, ‘CaopplicantIncome’, ‘LoanAmount’, ‘Loan_Amount_Term’, ‘Credit_History’, ‘Property_Area’]
    data = pandas.DataFrame(input_feature, columns=namaes)
    print(data)


data_scaled = scale.fit_transform(data)
data = pandas.DataFrame(data, columns=names)

# predictions using the loaded model file
Predictions = model.predict(data)
Print(prediction)
Prediction = int(prediction)
Print(type(prediction))

if (prediction == 0);
return render_template(“output.html”, result =”Loan
will
Not
be
Approved”)
else:
return render_template(“output.html”, result =”Loan
will
Not
be
Approved”)
# showing the prediction results in a UI

if__name__ ==”__main__”:
App.run(debug=False)  # running the app


