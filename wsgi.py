import os
from dotenv import load_dotenv
load_dotenv()

from Application import init_app

app = init_app()

if __name__ == "__main__":
	app.run(host=os.getenv('FLASK_ADDRESS'))