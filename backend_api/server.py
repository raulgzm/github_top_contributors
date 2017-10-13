# Python imports

# Core Flask imports

# Third-Party imports

# Apps Imports
from backend_api_app import app

if __name__ == "__main__":
	app.run(
		host='0.0.0.0', 
		port=9000, 
		debug=True
	)