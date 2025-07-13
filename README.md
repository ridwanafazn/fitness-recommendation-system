# Sistem Rekomendasi Latihan Fitness

- **Rule-based System**: Python `experta`
- **Optimization Algorithm**: Genetic Algorithm dengan Python `pygad`
---
## 📁 1. Dataset Latihan (Fitness Knowledge Base)

| Kolom               | Tipe Data   | Deskripsi |
|---------------------|-------------|-----------|
| `exercise_id`       | string      | ID unik untuk latihan |
| `exercise_name`     | string      | Nama latihan |
| `body_part`         | string      | Area tubuh (e.g. chest, shoulders) |
| `equipment`         | string[]    | Alat yang digunakan, bisa lebih dari satu |
| `primary_muscle`    | string      | Otot utama spesifik (e.g. front deltoids) |
| `secondary_muscle`  | string      | Otot pendukung spesifik (opsional) |
| `exercise_type`     | string      | Gaya eksekusi (e.g. bilateral_simultaneous) |
| `movement_type`     | string      | compound / isolation / cardio |
| `image_url`         | string      | URL gambar latihan |

---

## 👤 2. Data User

| Kolom              | Tipe Data   | Deskripsi |
|--------------------|-------------|-----------|
| `user_id`          | string      | ID unik user |
| `username`         | string      | Username, tidak perlu nama asli |
| `gender`           | string      | male / female |
| `weight_kg`        | float       | Berat badan |
| `height_cm`        | float       | Tinggi badan |
| `injuries`         | string[]    | Cedera (body part/muscle part) yang harus dihindari |

---

## 📝 3. Input Pembuatan Jadwal

Data yang dikirim user saat ingin membuat rencana latihan baru.

| Kolom                | Tipe Data   | Keterangan |
|----------------------|-------------|------------|
| `available_days`     | int         | Jumlah hari latihan per minggu (1–5) |
| `goals`              | string      | (Opsional) Muscle Gain / Fat Loss |
| `preferred_equipment`| string[]    | (Opsional) Alat yang tersedia. Jika kosong, semua alat diperbolehkan |
| `preferred_body_part`| string[]    | (Opsional) Area tubuh yang ingin difokuskan |

> ⚠️ Sistem akan menentukan metode split, dan menghindari otot berdasarkan `injuries`. User tidak memilih split, itu akan direkomendasikan engine.
---

## 📦 4. Format Output Rencana Latihan

Output berupa format JSON. Dengan menu latihan mingguan.

### Contoh Output

```json
{
  "split_type": "Push Pull Legs",
  "days": [
    {
      "day": day_1,
      "day_focus": "push",
      "exercises": [
        {
          "exercise_id": "ex001",
          "exercise_name": "Barbell Bench Press",
          "body_part": "chest",
          "primary_muscle": "pectoralis major",
          "secondary_muscle": "anterior deltoid",
          "equipment": ["barbell"],
          "image_url": "https://link.to/image.jpg"
        }
      ]
    },
    {
      "day": integer,
      "day_focus": "pull",
      "exercises": [ /* ... */ ]
    },
    {
      "day": day_2,
      "day_focus": "leg",
      "exercises": [ /* ... */ ]
    }
  ]
}
