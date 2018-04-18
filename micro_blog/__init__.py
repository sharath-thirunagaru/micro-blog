from flask import Flask
from micro_blog.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from micro_blog import routes