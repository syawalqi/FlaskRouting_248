from flask import Flask, request, redirect

app = Flask(__name__)

# Menyimpan data pengguna sementara (gunakan database untuk aplikasi nyata)
users = {}

@app.route('/')
def index():
    return """
    <h1>Welcome</h1>
    <p>Choose an option:</p>
    <div class="options">
        <a href="/login" class="btn">Login</a>
        <a href="/register" class="btn">Register</a>
    </div>
    """

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Simpan data register ke dalam dictionary
        users[username] = password
        return redirect('/login')
    
    return """
    <h1>Register</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        
        <button type="submit">Register</button>
    </form>
    """

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and users[username] == password:
            return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Redirect ke YouTube
        else:
            return "Login gagal, coba lagi."
    
    return """
    <h1>Login</h1>
    <form method="POST">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>
        
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>
        
        <button type="submit">Login</button>
    </form>
    """

if __name__ == '__main__':
    app.run(debug=True)
