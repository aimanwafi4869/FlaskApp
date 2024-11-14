from flask import Blueprint
import tensorflow as tf
import rclpy as rclpy
controller = Blueprint("ai", __name__, url_prefix="/api/ai")

@controller.route("/initialize")
def initializeAi():
    return 'initialize'