from app import app

# Runs the application
if __name__ == '__main__':
    app.secret_key = 'Buoj6FpNTHFOjix4MjVDjXYL5oSP95TZ0'
    app.config['SESSION_TYPE'] = "filesystem"
    app.run(debug=True)
