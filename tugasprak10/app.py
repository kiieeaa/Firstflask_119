from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Parsing parameter dari form
        nama = request.form.get('nama')
        umur = request.form.get('umur')
        
        # Validasi sederhana
        if nama and umur:
            try:
                umur = int(umur)
                result = f"Halo {nama}, umur Anda adalah {umur} tahun."
            except ValueError:
                result = "Mohon masukkan umur dengan angka yang valid."
        else:
            result = "Harap isi semua field."
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)