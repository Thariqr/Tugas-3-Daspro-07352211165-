# Data login yang disimpan dalam bentuk nested dictionary
data_login = {
    'mahasiswa122': {
        'password': 'test122',
        'email': 'coba122@gmail.com'
    },
    'mahasiswa222': {
        'password': 'test222',
        'email': 'coba222@gmail.com'
    },
    'mahasiswa322': {
        'password': 'test322',
        'email': 'coba322@gmail.com'
    },
    'mahasiswa422': {
        'password': 'test422',
        'email': 'coba422@gmail.com'
    },
    'mahasiswa522': {
        'password': 'test522',
        'email': 'coba522@gmail.com'
    },
    'mahasiswa123': {
        'password': 'test123',
        'email': 'coba123@gmail.com'
    },
    'mahasiswa223': {
        'password': 'test223',
        'email': 'coba223@gmail.com'
    },
    'mahasiswa323': {
        'password': 'test323',
        'email': 'coba323@gmail.com'
    },
    'mahasiswa423': {
        'password': 'test423',
        'email': 'coba423@gmail.com'
    },
    'mahasiswa523': {
        'password': 'test523',
        'email': 'coba523@gmail.com'
    }
}

# Fungsi untuk melakukan proses login
def login(username, password):
    if username in data_login and data_login[username]['password'] == password:
        print("Login berhasil.")
        print("Email yang terdaftar:", data_login[username]['email'])
    else:
        print("Login gagal. Periksa kembali username dan password Anda.")

# Contoh penggunaan
username_input = input("Masukkan username: ")
password_input = input("Masukkan password: ")
login(username_input, password_input)
