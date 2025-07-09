<<<<<<< HEAD
# 🎵 Hit Music Classifier

Uses **Machine Learning** to classify musics as **hits** or **non-hits**, based on audio features such as tempo, energy, duration, and popularity.

---

## 🚀 Features

✅ Data preprocessing with scaling  
✅ Trained models: Random Forest, XGBoost, Neural Network  
✅ Performance comparison between models  
✅ Saved pipeline (`scaler.pkl` and `random_forest_model.pkl`)  
✅ Web interface with Flask (`app.py`)  

---

## 📁 Project Structure

```
.
├── app.py                   # Flask web interface
├── data.csv                 # Dataset with song features
├── finalModel.ipynb         # Full pipeline and model comparison
├── RandomForest.ipynb       # Random Forest training
├── XGBoost.ipynb            # XGBoost training
├── NN.ipynb                 # Neural Network (Keras)
├── random_forest_model.pkl  # Saved classifier
├── scaler.pkl               # Saved scaler
└── templates/
    └── index.html           # Web page
```


---

## ⚙️ Installation

```bash
git clone https://github.com/goncaloalcobia/music-ml-classifier.git
cd music-ml-classifier
pip install -r requirements.txt
'''

## 🖥️ Run the Web Interface
```bash
python app.py
```

## 📊 Dataset

The dataset `data.csv` contains various features about songs, such as:

- Acousticness  
- Danceability  
- Energy  
- Instrumentalness  
- Liveness  
- Loudness  
- Speechiness  
- Tempo  
- Valence  
- Duration  
- Popularity (used to define hit or non-hit)

Songs are labeled as **hit** or **non-hit** based on a popularity threshold.

---

## 🧠 Models Used

✅ Random Forest  
✅ XGBoost  
✅ Neural Network (Keras)  

All models were trained and evaluated using scikit-learn pipelines with scaling, splitting, and performance metrics such as accuracy, precision, recall, F1-score, and ROC-AUC.

---

## 📜 License

This project is under the MIT License.


