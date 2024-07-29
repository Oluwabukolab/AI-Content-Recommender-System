from waitress import serve
import app

if __name__ == '__main__':
    print("Starting the Waitress server on http://localhost:8080")
    serve(app.app, host='0.0.0.0', port=8080)
