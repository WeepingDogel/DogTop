from flask import Flask, render_template, jsonify
import psutil


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def home_page():
        return render_template('index.html')  # Renders the index.html template for the home page

    @app.route('/get_cpu')
    def get_cpu_rate():
        cpu_percentages = []
        for _ in range(10):
            cpu_percentages.append(psutil.cpu_percent(interval=1))  # Appends CPU usage percentage to the list

        return jsonify(cpu_percentages)  # Returns the CPU usage percentages as a JSON response

    @app.route('/get_mem')
    def get_mem_rate():
        memory_usage = psutil.virtual_memory().percent  # Retrieves the current memory usage percentage
        return jsonify({'memory_usage': memory_usage})  # Returns the memory usage as a JSON response

    @app.route('/get_max_mem')
    def get_max_mem():
        max_memory = psutil.virtual_memory().total / 1024 / 1024 / 1024  # Calculates the maximum memory usage in GB
        return jsonify({'max_memory': round(max_memory)})  # Returns the maximum memory usage as a JSON response

    @app.route('/get_disk')
    def get_disk_rate():
        disk_usage = psutil.disk_usage('/').percent  # Retrieves the current disk usage percentage

        return jsonify({'disk_usage': disk_usage})  # Returns the disk usage as a JSON response

    @app.route('/get_disk_total')
    def get_disk_total():
        disk_total = psutil.disk_usage('/').total / 1024 / 1024 / 1024  # Calculates the total disk capacity in GB
        return jsonify({'disk_total': disk_total})  # Returns the total disk capacity as a JSON response

    return app
