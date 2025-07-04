# Sistem Rekomendasi Latihan Fitness

- **Rule-based System**: Python `experta`
- **Optimization Algorithm**: Genetic Algorithm dengan Python `DEAP`

---

## 📁 1. Dataset Latihan (Fitness Knowledge Base)

| Kolom               | Tipe Data   | Deskripsi |
|---------------------|-------------|-----------|
| `exercise_id`       | string      | ID unik untuk latihan |
| `exercise_name`     | string      | Nama latihan |
| `body_part`         | string      | Area tubuh (e.g. chest, shoulder) |
| `equipment`         | string[]    | Alat yang digunakan, bisa lebih dari satu |
| `primary_muscle`    | string      | Otot utama spesifik (e.g. anterior deltoid) |
| `secondary_muscle`  | string      | Otot pendukung spesifik (opsional) |
| `exercise_type`     | string      | Gaya eksekusi (e.g. bilateral_simultaneous) |
| `movement_type`     | string      | Compound / Isolation / Cardio |
| `image_url`         | string      | URL gambar latihan |

---

## 👤 2. Data User

| Kolom              | Tipe Data   | Deskripsi |
|--------------------|-------------|-----------|
| `user_id`          | string      | ID unik user |
| `username`         | string      | Username, tidak perlu nama asli |
| `age`              | int         | Usia |
| `gender`           | string      | male / female |
| `weight_kg`        | float       | Berat badan |
| `height_cm`        | float       | Tinggi badan |
| `injuries`         | string[]    | Cedera (body part/muscle part) yang harus dihindari |

---

## 📝 3. Input Pembuatan Jadwal

Data yang dikirim user saat ingin membuat rencana latihan baru.

| Kolom                | Tipe Data   | Keterangan |
|----------------------|-------------|------------|
| `plan_name`          | string      | Nama rencana latihan (input) |
| `available_days`     | int         | Jumlah hari latihan per minggu (1–5) |
| `goals`              | string      | (Opsional) Muscle Gain / Fat Loss |
| `preferred_equipment`| string[]    | (Opsional) Alat yang tersedia. Jika kosong, semua alat diperbolehkan |
| `preferred_body_part`| string[]    | (Opsional) Area tubuh yang ingin difokuskan |

> ⚠️ Sistem akan menentukan split style, metode set, dan menghindari otot berdasarkan `injuries`. User tidak memilih split maupun metode latihan, itu akan direkomendasikan engine.

---

## 📦 4. Format Output Rencana Latihan

Output berupa format JSON. Bisa mingguan (jika ≥2 hari tersedia) atau berskala lebih panjang (misal 1x/minggu selama 3 minggu).

### Contoh Output JSON

```json
{
  "routines_id" : uuid
  "plan_name": "Build Strength Routine",
  "creator": "username"
  "split_type": "Push Pull Legs",
  "recommended_methods": ["Superset", "Normal"],
  "days": [
    {
      "day": "Senin",
      "focus_area": "Push",
      "exercises": [
        {
          "exercise_id": "ex001",
          "exercise_name": "Barbell Bench Press",
          "exercise_type": "bilateral_simultaneous",
          "body_part": "chest",
          "primary_muscle": "pectoralis major",
          "secondary_muscle": "anterior deltoid",
          "movement_type": "compound",
          "equipment": ["barbell"],
          "rep_range": "6-10",
          "rest_range": "90-120",
          "image_url": "https://link.to/image.jpg"
        },
        {
          "exercise_id": "ex045",
          "exercise_name": "Dumbbell Lateral Raise",
          "exercise_type": "bilateral_simultaneous",
          "body_part": "shoulders",
          "primary_muscle": "lateral deltoid",
          "secondary_muscle": null,
          "movement_type": "isolation",
          "equipment": ["dumbbell"],
          "rep_range": "12-15",
          "rest_range": "45-60",
          "image_url": "https://link.to/image2.jpg"
        }
      ]
    },
    {
      "day": "Kamis",
      "focus_area": "Pull",
      "exercises": [ /* ... */ ]
    },
    {
      "day": "Sabtu",
      "focus_area": "Leg",
      "exercises": [ /* ... */ ]
    }
  ]
}
