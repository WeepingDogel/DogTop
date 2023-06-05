## DogTop

DogTop is a WebPanel that displays the status of CPU, Memory, and Disk. It provides real-time monitoring of system resources using Flask and Echartjs.

## ScreenShot

![](/Screenshot.png)

## Features

- CPU Usage: View the current CPU usage as a percentage.
- Memory Usage: Monitor the current memory usage as a percentage.
- Maximum Memory: Get the maximum memory usage supported by the system in GB.
- Disk Usage: Check the current disk usage as a percentage.
- Total Disk Capacity: Get the total disk capacity in GB.

## Prerequisites

Before running DogTop, ensure you have the following installed:

- Python 3
- Flask
- psutil
- Echartjs

## Installation and Usage
1. Clone the repository:
```
git clone https://github.com/your-username/DogTop.git
```
2. Navigate to the project directory:
```
cd DogTop/flaskr
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```
4. Start the application:
```
flask run
```
5. Open your web browser and access the application at `http://localhost:5000`.

## Project Structure

The project structure should look like this:
```
flaskr
├── init.py
├── pycache
│ └── init.cpython-311.pyc
├── static
│ └── echart.js
└── templates
└── index.html

4 directories, 4 files
```

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please submit an issue or a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
