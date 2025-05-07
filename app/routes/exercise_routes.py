from flask import Blueprint, jsonify
from app.services.data_loader import load_exercise_data

exercise_routes = Blueprint('exercise_routes', __name__)

@exercise_routes.route('/api/exercises', methods=['GET'])
def get_exercises():
    # Memuat data latihan dari file CSV
    exercise_data = load_exercise_data('data/exercise_dataset.csv')
    
    # Cek jika data berhasil dimuat
    if isinstance(exercise_data, dict) and exercise_data.get('error'):
        return jsonify(exercise_data), 500
    
    # Mengonversi DataFrame menjadi list of dictionaries
    exercises_list = exercise_data.to_dict(orient='records')
    
    return jsonify(exercises_list), 200
