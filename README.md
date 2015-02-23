# Flask template for Google App Engine

A template for use [Flask (a Python microframework)](http://flask.pocoo.org/)
in Google App Engine.


## Requirements
* Python 2.7
* pip
* [Google App Engine SDK for Python](https://cloud.google.com/appengine/downloads)


## Run the project locally
1. Clone this repository.

2. Install dependencies in the project's `lib` directory. Run this command
inside the project folder:
   ```
   pip install -r requirements.txt -t lib
   ```

3. Run the app with _GoogleAppEngineLauncher_ or from command line:
   ```
   dev_appserver.py .
   ```

4. Open [http://localhost:8080](http://localhost:8080). Hello world!
