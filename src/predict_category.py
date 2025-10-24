# src/predict_category.py

import pickle

# 1. Încarcăm modelul și vectorizatorul 
try:
    with open("models/product_category_model.pkl", "rb") as f:
        vectorizer, model = pickle.load(f)
    print(" Model încărcat cu succes!")
except FileNotFoundError:
    print("❌ Modelul nu a fost găsit. Asigură-te că 'product_category_model.pkl' există în folderul 'models'.")
    exit()

#  2. Funcție de predicție 
def predict_category(title):
    X = vectorizer.transform([title])
    return model.predict(X)[0]

#  3. Interfață interactivă 
if __name__ == "__main__":
    print("Introduceți titlul produsului pentru predicție. Scrieți 'exit' pentru a ieși.\n")
    while True:
        user_input = input("Titlu produs: ")
        if user_input.lower() == "exit":
            print("Program încheiat.")
            break
        prediction = predict_category(user_input)
        print(f"Predicție categorie: {prediction}\n")