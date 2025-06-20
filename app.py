from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

#importing pickle files
model = pickle.load(open('classifier.pkl','rb'))
ferti = pickle.load(open('fertilizer.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@ app.route('/Mod')
def Mod():
    return render_template('Mod.html')

@ app.route('/final_model')
def final_model():
    return render_template('final_model.html')



@app.route('/predict',methods=['POST'])
def predict():
    temp = request.form.get('temp')
    humi = request.form.get('humid')
    mois = request.form.get('mois')
    soil = request.form.get('soil')
    crop = request.form.get('crop')
    nitro = request.form.get('nitro')
    pota = request.form.get('pota')
    phosp = request.form.get('phos')
    if None in (temp, humi, mois, soil, crop, nitro, pota, phosp) or not all(val.isdigit() for val in (temp, humi, mois, soil, crop, nitro, pota, phosp)):
        return render_template('Mod.html', x='Invalid input. Please provide numeric values for all fields.')

# Convert values to integers
    input = [int(temp), int(humi), int(mois), int(soil), int(crop), int(nitro), int(pota), int(phosp)]
    res = ferti.classes_[model.predict([input])]
    return render_template('Mod.html', x=res)
if __name__ == "__main__":
    app.run(debug=True)