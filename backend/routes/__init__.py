from flask import Blueprint

# Import route blueprints
from backend.routes.tasks import tasks_bp
from backend.routes.pet import pet_bp

__all__ = ['tasks_bp', 'pet_bp']
