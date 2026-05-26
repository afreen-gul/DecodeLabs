import pickle

# Load Trained Model
with open("models/classifier.pkl", "rb") as file:
    model = pickle.load(file)

flower_names = [

    "Setosa",
    "Versicolor",
    "Virginica"
]

def predict_flower(features):

    prediction = model.predict([features])[0]

    return flower_names[prediction]