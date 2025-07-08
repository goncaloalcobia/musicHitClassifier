from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

# Carregar o modelo e scaler
clf = pickle.load(open('random_forest_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Inicializar Spotipy
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='SEU_CLIENT_ID',  # 🟢 Substitui pelos teus
    client_secret='SEU_CLIENT_SECRET'  # 🟢 Substitui pelos teus
))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        spotify_url = request.form['spotify_url']
        evaluator = request.form['evaluator']

        # Obter ID do Spotify
        track_id = spotify_url.split('/')[-1].split('?')[0]

        # Obter dados da música
        track_info = sp.track(track_id)
        track_name = track_info['name']
        artist_name = track_info['artists'][0]['name']

        # Aqui o resto do teu código de previsão (features, scaler, etc.)
        # Exemplo:
        # X_new = scaler.transform(np.array([feature_list]))
        # prob = clf.predict_proba(X_new)[:, 1][0]
        # pred = int(prob > threshold)

        # Devolve para o HTML
        return render_template(
            'index.html',
            prediction=pred,
            probability=prob,
            threshold=threshold,
            evaluator_choice=evaluator,
            track_name=track_name,
            artist_name=artist_name
        )

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
