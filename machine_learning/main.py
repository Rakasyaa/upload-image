import tensorflow as tf
import numpy as np
from keras._tf_keras.keras.preprocessing import image
from flask import Flask, jsonify, request
from flask_cors import CORS
import cv2
import os

class_names = [
    'Jerawat',
    'Karsinoma',
    'Dermatitis Atopik',
    'Selulitis',
    'Eksim',
    'Eksantema',
    'Herpes',
    'Pigmentasi',
    'Lupus',
    'Melanoma',
    'Dermatitis',
    'Psoriasis',
    'Keratosis',
    'Penyakit Sistemik',
    'Infeksi Jamur',
    'Biduran',
    'Tumor Vaskular',
    'Vaskulitis',
    'Kutil'
]
penjelasan = [
    'Peradangan kelenjar minyak yang menyebabkan bintik merah, bernanah, atau komedo.',
    'Kanker kulit sel basal/sel skuamosa akibat paparan sinar UV berlebihan.',
    'Peradangan kulit kronis dengan gejala gatal, kemerahan, dan kulit kering.',
    'Infeksi bakteri pada kulit dan jaringan di bawahnya yang menyebabkan kemerahan, bengkak, dan nyeri.',
    'Kondisi kulit meradang dengan gejala gatal, kemerahan, dan terkadang lepuh.',
    'Ruam kulit yang sering menyertai infeksi virus (seperti campak atau demam berdarah).',
    'Infeksi virus HSV dengan gejala lepuh berkelompok dan nyeri pada kulit/mukosa.',
    'Gangguan warna kulit seperti hiperpigmentasi (gelap) atau hipopigmentasi (pucat).',
    'Penyakit autoimun yang bisa menyebabkan ruam berbentuk kupu-kupu di wajah (lupus eritematosus).',
    'Kanker kulit ganas yang berasal dari melanosit (sel penghasil pigmen).',
    'Peradangan kulit umum dengan gejala kemerahan, gatal, dan iritasi.',
    'Penyakit autoimun dengan kulit bersisik tebal berwarna keperakan.',
    'Penebalan kulit keratin, seperti keratosis aktinik (pra-kanker akibat sinar UV).',
    'Kondisi kulit yang terkait dengan penyakit dalam (misal: diabetes, lupus).',
    'Infeksi seperti panu, kutu air, atau kurap yang disebabkan oleh jamur.',
    'Reaksi alergi dengan bilur merah gatal (urtikaria) yang muncul tiba-tiba.',
    'Pertumbuhan abnormal pembuluh darah di kulit (seperti hemangioma).',
    'Peradangan pembuluh darah yang bisa menyebabkan ruam atau luka kulit.',
    'Pertumbuhan kulit kecil akibat infeksi virus HPV.'
]
penanganan = [
    'Bersihkan wajah 2x sehari, hindari memencet jerawat, gunakan produk non-comedogenic, dan konsultasi dokter untuk obat topikal/oral.',
    'Bedah eksisi, terapi radiasi, krioterapi, atau terapi fotodinamik. Hindari paparan matahari langsung.',
    'Gunakan pelembab hypoallergenic, hindari pemicu alergi, obat kortikosteroid topikal, dan antihistamin.',
    'Antibiotik oral/IV, kompres hangat, istirahat, dan elevasi area yang terkena.',
    'Hindari iritan, gunakan pelembab, kompres dingin, dan obat topikal (seperti kortikosteroid).',
    'Pengobatan sesuai penyebab (antivirus jika perlu), kompres dingin, dan obat penurun demam.',
    'Antivirus (seperti asiklovir), jaga kebersihan area, hindari kontak langsung dengan orang lain.',
    'Gunakan tabir surya, krim pencerah (untuk hiperpigmentasi), atau terapi laser.',
    'Kortikosteroid, imunosupresan, hindari sinar matahari, dan kontrol rutin ke rheumatologist.',
    'Pembedahan, imunoterapi, terapi target, atau kemoterapi tergantung stadium.',
    'Hindari iritan, gunakan pelembab, kompres dingin, dan obat topikal (seperti kortikosteroid).',
    'Terapi topikal (vitamin D analog), fototerapi, atau obat sistemik untuk kasus berat.',
    'Krioterapi, krim imiquimod, atau terapi laser. Gunakan tabir surya secara rutin.',
    'Pengobatan penyakit dasar, konsultasi dokter spesialis terkait, dan perawatan kulit suportif.',
    'Antijamur topikal/oral (seperti klotrimazol), jaga kebersihan, dan hindari kelembaban berlebih.',
    'Antihistamin, hindari pemicu alergi, dan kompres dingin untuk mengurangi gatal.',
    'Terapi laser, obat oral (propranolol), atau operasi untuk kasus yang mengganggu.',
    'Kortikosteroid, imunosupresan, dan pengobatan penyebab dasar (jika ada).',
    'Krioterapi, asam salisilat, atau operasi kecil. Jaga kebersihan untuk mencegah penyebaran.'
]

app = Flask(__name__)
CORS(app)

model_path = 'cnn_model.h5'
cnn_model = tf.keras.models.load_model(model_path)

@app.route('/predict', methods=['POST'])
def predictions():
    if 'photo' not in request.files:
        return jsonify({'status': 400, 'message': 'No file part in the request'})

    file = request.files['photo']
    if file.filename == '':
        return jsonify({'status': 400, 'message': 'No selected file'})

    file_path = "uploads/" + file.filename
    try:
        file.save(file_path)
    except Exception as e:
        return jsonify({'status': 500, 'message': 'File saving failed', 'error': str(e)})

    try:
        images= []
        img_size = (192, 192, 3)
        
        img_path = file_path
        
        
        img = image.load_img(img_path, target_size=img_size)
        img = image.img_to_array(img)
        img_array = np.asarray(cv2.resize(cv2.imread(img_path, cv2.IMREAD_COLOR), img_size[0:2])[:, :, ::-1])
        images.append(img_array)
        images = np.asarray(images)
        
        predictions = cnn_model.predict(images, verbose=0)[0]
        
        result_index = np.argmax(predictions)
        result = {
            'nama_penyakit': class_names[result_index],
            'penjelasan': penjelasan[result_index],
            'penanganan': penanganan[result_index]
        }      
        os.remove(file_path)

        return jsonify({'status': 200, 'message': 'Prediction Success', 'prediction': result})
    except Exception as e:
        if os.path.exists(file_path):
            os.remove(file_path)
        return jsonify({'status': 500, 'message': 'Prediction failed', 'error': str(e)})

@app.route('/hello', methods=['GET'])
def hello():
    return "hello world"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))