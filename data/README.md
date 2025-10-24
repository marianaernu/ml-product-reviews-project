# ml-product-reviews-project
Acest proiect dezvoltă un model de învățare automată care prezice categoria unui produs pe baza titlului său. 
Scopul este de a automatiza clasificarea produselor într-un magazin online și de a reduce timpul de muncă manuală.

## Structura proiectului
```my project
ml-product-reviews-project/
│
├── data/ # Setul de date folosit pentru antrenare
│ └── products.csv
├── models/ # Modele antrenate
│ └── product_category_model.pkl
├── src/ # Scripturi Python
│ ├── train_model.py # Antrenează și salvează modelul
│ └── predict_category.py # Testare interactivă
├── notebooks/ 
│ └── nproduct_analysis.ipynb

└── README.md # Documentația proiectului

## Cerințele necesare folosite in proiect
- Python  
- Librării: pandas, scikit-learn  
- Recomandat: Jupyter sau VS Code pentru notebook

## Instalare
```
1. Am clonat repozitoriul : git clone https://github.com/marianaernu/ml-product-reviews-project.git
cd ml-product-reviews-project

2. Am instalat librariile necesare:
   pip install pandas scikit-learn

## Rulare

1. Antrenarea modelului:
   python src/train_model.py
Am creat  fișierul: models/product_category_model.pkl

2. Predictia categoriilor produselor:
   python src/predict_category.py
    Aici intoducem titlul produsului sau scriem exit sa iesim din script.

##  Concluzie

Proiectul dat demonstrează cum se poate utiliza învățarea automată pentru clasificarea automată a produselor pe categorii, pe baza titlului.  

Modelul antrenat oferă o acuratețe bună pentru categoriile principale și poate fi extins cu date suplimentare pentru o performanță și mai mare.  

Prin automatizarea acestui proces, echipa de listare a produselor poate economisi timp și reduce erorile umane, îmbunătățind experiența utilizatorilor pe platformă.