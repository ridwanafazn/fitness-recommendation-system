# 📊 Struktur Data Sistem Rekomendasi Latihan Fitness

1. **Rule-based system** : python Experta dan
2. **Optimization algorithm** : Genetic Algorithm with python DEAP

---

## ✅ 1. Dataset Fitness Knowledge (Latihan)

| Kolom              | Tipe Data   | Deskripsi |
|--------------------|-------------|-----------|
| `exercise_id`      | string/int  | ID unik latihan |
| `exercise_name`    | string      | Nama latihan |
| `muscle_group`     | string      | Otot utama yang dilatih |
| `secondary_muscle` | string      | Otot pendukung |
| `type`             | string      | Compound / Isolation / Cardio |
| `equipment`        | string      | Alat yang dibutuhkan |
| `difficulty_level` | string      | Beginner / Intermediate / Advanced |
| `rep_min`          | int         | Reps minimal disarankan |
| `rep_max`          | int         | Reps maksimal disarankan |
| `rest_min`         | int (sec)   | Minimal rest time |
| `rest_max`         | int (sec)   | Maksimal rest time |

---

## ✅ 2. Data Akun User

| Kolom               | Tipe Data | Deskripsi |
|---------------------|-----------|-----------|
| `user_id`           | string    | ID unik user |
| `name`              | string    | Nama user |
| `age`               | int       | Usia |
| `gender`            | string    | L / P |
| `weight_kg`         | float     | Berat badan |
| `height_cm`         | float     | Tinggi badan |
| `experience_level`  | string    | Beginner / Intermediate / Advanced |
| `injuries`          | string[]  | Daftar cedera bila ada |

---

## ✅ 3. Preferensi untuk Generate Jadwal (Filter Input)

> Data ini dikirim saat user ingin membuat jadwal baru.

| Kolom               | Tipe Data | Deskripsi |
|---------------------|-----------|-----------|
| `plan_name`         | string    | Nama jadwal latihan |
| `goals`             | string    | Muscle Gain / Fat Loss / Maintenance |
| `available_days`    | int       | Jumlah hari latihan per minggu |
| `day_split_style`   | string    | Full Body / Upper-Lower / PPL |
| `duration_per_day`  | int (min) | Durasi latihan per hari |
| `equipment_access`  | string[]  | Alat yang tersedia |
| `preferred_muscles` | string[]  | Fokus otot utama (optional) |
| `avoid_muscles`     | string[]  | Otot yang ingin dihindari (optional) |
| `preferred_methods` | string[]  | Normal / Drop Set / Superset / HIIT |

---

## ✅ 4. Format Output Jadwal Latihan

Output dari sistem berbentuk jadwal mingguan, disesuaikan dengan filter dan akun user.

### 📁 Contoh Output JSON

```json
{
  "plan_name": "Bulking 3x Seminggu",
  "days": [
    {
      "day": "Senin",
      "focus_area": "Push",
      "exercises": [
        {
          "exercise_name": "Barbell Bench Press",
          "sets": 4,
          "reps": 10,
          "rest_time": 90,
          "method": "Normal Set",
          "equipment": "Barbell"
        },
        {
          "exercise_name": "Incline Dumbbell Press",
          "sets": 3,
          "reps": 10,
          "rest_time": 75,
          "method": "Normal Set",
          "equipment": "Dumbbell"
        },
        {
          "exercise_name": "Shoulder Press",
          "sets": 3,
          "reps": 12,
          "rest_time": 60,
          "method": "Normal Set",
          "equipment": "Machine"
        },
        {
          "exercise_name": "Lateral Raise",
          "sets": 3,
          "reps": 15,
          "rest_time": 60,
          "method": "Drop Set",
          "equipment": "Dumbbell"
        },
        {
          "exercise_name": "Triceps Pushdown",
          "sets": 3,
          "reps": 12,
          "rest_time": 60,
          "method": "Normal Set",
          "equipment": "Cable"
        }
      ]
    },
    {
      "day": "Rabu",
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
