from app import app  # This imports the app object from the 'app' module

print("Running Flask app...")

if __name__ == "__main__":
    app.run(debug=True)  # Starts the Flask app in debug mode
