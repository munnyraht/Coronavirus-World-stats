from flask import Flask

app = Flask(__name__)

from coronavirus_world_stats import routes
