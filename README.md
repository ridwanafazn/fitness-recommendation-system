# Sistem Rekomendasi Latihan Fitness

## Ringkasan Proses Sistem

| Tahap / Komponen               | Input Utama                                          | Output Utama                               | Deskripsi & Rule Inti                                                                                       |
|-------------------------------|-----------------------------------------------------|--------------------------------------------|------------------------------------------------------------------------------------------------------------|
| **1. Dataset Latihan Fitness** | `dataset_fitness_7_glossary_match.csv`               | DataFrame `df` latihan                      | Data latihan berisi kolom: `exercise_id`, `exercise_name`, `body_part`, `equipment` (list), `primary_muscle`, `secondary_muscle`, dll. Digunakan sebagai knowledge base. |
| **2. Mapping Muscle ke Body Part** | Kolom `primary_muscle`, `secondary_muscle`          | Mapping `muscle_to_body_part`               | Otot spesifik di-mapping ke kelompok body part umum (e.g. front deltoids → shoulders) untuk filter dan penyesuaian cedera.|
| **3. Input User**              | `user_input` dict berisi: `age`, `gender`, `bmi`, `injuries` (list), `available_days`, `goals`, `preferred_body_part`, `preferred_equipment` | User fact di `UserInput` pada Experta      | Data user dikemas untuk rule-based system sebagai input pengambilan keputusan split dan jadwal fokus otot.  |
| **4. Rule-Based System (Experta)** | `UserInput` fact                                     | `Recommendation` fact: `split_method`, `schedule` dict harian | Berdasarkan jumlah `available_days`, `gender`, dan `bmi`, sistem menentukan metode split (`fullbody`, `upperlower`, `ppl`, `ppl+focus`) dan jadwal fokus tiap hari (e.g. push, pull, legs, cardio). Jika BMI ≥ 25, cardio disisipkan secara otomatis menggantikan fokus kaki atau fullbody pada beberapa hari. Cedera (`injuries`) dihindari. |
| **5. Mapping Split ke Fokus Harian** | `split_method` (string), `available_days` (int), `schedule` dari RBS (optional) | List `focus_areas` per hari               | Fungsi `map_split_to_schedule` memetakan split yang dipilih menjadi daftar fokus per hari seperti ['push', 'pull', 'legs', 'cardio'] sesuai aturan dan output RBS. |
| **6. Mapping Cedera ke Body Parts** | `user_input["injuries"]` (list)                      | Set `injured_body_parts`                    | Fungsi `map_injury_to_body_parts` mengkonversi list cedera (bisa berupa otot/spesifik atau body part) menjadi set body part yang harus dihindari latihan. |
| **7. Filtering Pool Latihan per Hari** | DataFrame `df` latihan, `focus` hari (e.g. push), `injured_body_parts`, `preferred_equipment` | DataFrame `daily_exercise_pool[day]`        | Fungsi `get_daily_exercise` menyaring latihan berdasarkan: <br> - Hindari cedera (body_part ∉ injured_body_parts) <br> - Fokus latihan sesuai hari (misal chest untuk push) <br> - Filter alat sesuai preferensi user (jika ada), fallback ke body weight jika terlalu ketat <br> - Minimal 5 latihan per hari (fallback bertingkat) |
| **8. Gabung Pool Latihan Harian** | `daily_exercise_pool`                                | DataFrame `exercises_pool` unik              | Semua pool latihan dari tiap hari digabung dan dideduplikasi berdasarkan `exercise_id` sebagai kumpulan kandidat latihan untuk optimasi. |
| **9. Optimasi Genetic Algorithm (GA) per Hari** | Pool latihan per hari, `focus` hari, `injured_body_parts`, `bmi` | Solusi terbaik (`daily_selected_exercises`) per hari | GA menggunakan `pygad` dengan fitness function khusus: <br> - Penalti latihan yang melibatkan cedera <br> - Penalti jika latihan tidak fokus pada target hari <br> - Penalti duplikasi body part dalam hari yang sama <br> - Pembatasan khusus untuk latihan cardio run (maksimal 1 run per hari), dan indoor cardio maksimal 1-2 per hari <br> - Preferensi alat dan variasi otot dipertimbangkan <br> Output berupa set latihan optimal per hari. |
| **10. Format Output Jadwal Mingguan** | `daily_selected_exercises` dan data split               | JSON terstruktur rencana latihan lengkap    | Output akhir berformat JSON, berisi <br> - `plan_name`, `split_type` <br> - Daftar hari dengan fokus (push, pull, legs, cardio) <br> - Daftar latihan per hari lengkap dengan `exercise_id`, `exercise_name`, `body_part`, `primary_muscle`, `secondary_muscle`, `equipment`, `image_url` |

---

## Contoh Variabel Kunci

| Variabel                     | Tipe / Struktur                    | Keterangan                                       |
|------------------------------|----------------------------------|-------------------------------------------------|
| `user_input`                 | dict                             | Input data user untuk rule-based system          |
| `Recommendation`             | Fact (Experta)                   | Output rule-based split dan jadwal fokus          |
| `schedule`                   | dict                             | Jadwal fokus per hari, contoh `{ 'day_1': 'push' }` |
| `daily_exercise_pool`        | dict of DataFrame                | Latihan yang sudah difilter per hari               |
| `exercises_pool`             | DataFrame                       | Gabungan latihan unik seluruh minggu              |
| `daily_selected_exercises`   | dict of list of DataFrame rows  | Latihan terbaik hasil GA per hari                   |
| `daywise_schedule`           | dict                            | Jadwal latihan lengkap dengan data latihan terperinci|

---

## Catatan Khusus

- Rule-based system sangat krusial menentukan split dan penyesuaian jadwal berdasarkan data user dan cedera.
- Optimasi GA berjalan per hari (hybrid modular) agar solusi lebih fokus dan relevan.
- Fallback filter latihan menjamin pool latihan minimal cukup walau preferensi user ketat.
- Output akhir siap langsung dikonsumsi oleh frontend dan API backend.

