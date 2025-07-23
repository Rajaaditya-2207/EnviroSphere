# EnviroSphere 🌍

![GitHub language count](https://img.shields.io/github/languages/count/Rajaaditya-2207/EnviroSphere?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/Rajaaditya-2207/EnviroSphere?style=for-the-badge&color=blue)
![GitHub repo size](https://img.shields.io/github/repo-size/Rajaaditya-2207/EnviroSphere?style=for-the-badge)

An interactive, full-stack web application for climate change awareness. This project features a **Flask backend** that receives, processes, and visualizes live environmental data sent from a connected **IoT device**.

**[Live Demo](https://rajaaditya-2207.github.io/EnviroSphere/)**

***

## ✨ About The Project

EnviroSphere is more than just an informational website; it's a real-time environmental monitoring system. The core of the project is a data pipeline where an IoT device records environmental data and transmits it to the Flask web server.

The server then processes this data to plot interactive graphs for live display on the website, offering a dynamic look into current environmental conditions. The goal is to provide a practical tool for data collection and analysis while educating users on the critical aspects of climate change.

![EnviroSphere Screenshot](https://user-images.githubusercontent.com/97828612/232230689-548c783c-f458-4503-be87-575796a5b67a.png)
*(Note: I've used a screenshot from a similar project for demonstration. You can replace the URL with a screenshot of your own project.)*

***

## 💡 How It Works

The project follows a simple yet powerful data flow:

1.  **Data Collection:** An IoT device equipped with sensors records key environmental data (e.g., temperature, humidity, air quality).
2.  **Data Transmission:** The device sends this data to a dedicated API endpoint on the Flask server.
3.  **Backend Processing:** The Flask server receives the data, stores it, and uses plotting libraries to generate visualizations.
4.  **Live Display:** The front end displays these graphs, providing a live, interactive dashboard of the environmental data.
5.  **Data Archiving:** The server automatically saves the raw data in **CSV** format and the graphs as **PNG** images, creating a historical record for future analysis.

***

## 🚀 Features

* **IoT Data Integration:** Receives and processes real-time data from a connected environmental monitoring device.
* **Live Data Visualization:** Plots incoming data into interactive graphs on the web interface.
* **Data Export:** Automatically converts and saves collected data as CSV files and graphs as PNG images.
* **ML-Ready Dataset:** The collected data is structured for future use in data processing and machine learning applications.
* **Responsive Design:** Fully functional and visually appealing on all devices, from mobile phones to desktops.

***

## 🛠️ Built With

* **Backend & Data Processing:**
    * ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
    * ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
* **Frontend:**
    * ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
    * ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
    * ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
* **Hardware (Conceptual):**
    * IoT Device (e.g., ESP32, Raspberry Pi) with sensors.

***

## 🔮 Future Scope

The data archiving feature opens up exciting possibilities for future development:

* **Advanced Data Analysis:** Implement more complex data processing and statistical analysis on the collected dataset.
* **Machine Learning Models:** Use the historical data to train ML models for trend prediction, anomaly detection, or forecasting environmental changes.
* **Dataset Development:** After a significant period of data collection, the compiled dataset can be published for academic or research purposes.

***

## ⚙️ Getting Started

To get a local copy of the web server up and running, follow these steps.

### Prerequisites

* Python 3.x and pip must be installed.
* Setup for the companion IoT device is separate. The server expects to receive data at pre-configured API endpoints.

### Installation

1.  **Clone the repository**:
    ```sh
    git clone [https://github.com/Rajaaditya-2207/EnviroSphere.git](https://github.com/Rajaaditya-2207/EnviroSphere.git)
    ```
2.  **Navigate to the project directory**:
    ```sh
    cd EnviroSphere
    ```
3.  **Create and activate a virtual environment**:
    * For Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * For macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```
4.  **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```
5.  **Run the Flask application**:
    ```sh
    flask run
    ```
6.  **View the website**: Open your browser and go to `http://127.0.0.1:5000`.

***

## 🤝 Contributing

Contributions are greatly appreciated. If you have a suggestion that would make this better, please fork the repo and create a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

***

## 📄 License

Distributed under the MIT License. It's a good practice to add a `LICENSE` file to your repository.

***

## 📬 Contact

**Rajaaditya**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rajaaditya-r-696285330)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Rajaaditya-2207)

Project Link: [https://github.com/Rajaaditya-2207/EnviroSphere](https://github.com/Rajaaditya-2207/EnviroSphere)
