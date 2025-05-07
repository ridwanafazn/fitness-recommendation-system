import pandas as pd

def load_exercise_data(file_path):
    try:
        # Membaca file CSV dan mengembalikan data dalam bentuk DataFrame
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        return {"error": str(e)}
