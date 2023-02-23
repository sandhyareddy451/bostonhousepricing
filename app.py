import pickle
from flask import Flask, jsonify, url_for,request, app, render_template



app=Flask(__name__)
#load the model
regmodel=pickle.load(open('regmodel.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict_api', methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())[0]).reshape(1,-1))
    new_data=scalar.transform(np.array(list(data.values())[0]).reshape(1,-1))
if __name__=='__main__':
    app.run(debug=True)