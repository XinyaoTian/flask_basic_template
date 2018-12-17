from app import create_app
# command reinforcement
from app import cli

app = create_app()
cli.register(app)
