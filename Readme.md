# 🚀 Flask Cache Proxy

![Flask Cache Proxy](https://img.shields.io/badge/built%20with-Flask-red.svg) ![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)

## 📝 Overview

*Flask Cache Proxy* is a simple yet powerful web application that acts as a caching proxy server using Flask. It fetches content from specified URLs and caches the responses for a defined duration to enhance performance and minimize load times. 🌐✨
[Caching Proxy](https://roadmap.sh/projects/caching-server)

## 🌟 Features

- *Caching Mechanism:* 🗄️ Utilizes a Time-To-Live (TTL) cache to store responses, significantly reducing the need for repeated network calls.
- *Dynamic Routing:* 📡 Supports dynamic URL path routing, allowing the retrieval of content from any accessible URL.
- *Cache Hit/Miss Logging:* 📊 Provides real-time feedback on cache performance, indicating whether responses are served from cache or fetched fresh.
- *Command-line Configuration:* ⚙️ Easily configurable port for running the application.

## 🚀 Getting Started

### 📋 Prerequisites

Ensure that you have Python 3.7 or higher installed on your machine.

### 💻 Installation

- Clone the repository to your local machine.
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

- Install the necessary packages to set up the project environment.
    ```bash
    pip install -r requirements.txt
    ```


### 🛠️ Usage

- Launch the application and specify the desired port for operation.
    ```bash
    python app.py --port <PORT_NUMBER>
    ```

- Access the caching proxy by navigating to the application's URL with the target URL appended.
    ```bash
    curl http://localhost:5000/<YOUR_URL_PATH>
    ```


### 🔍 Example

You can fetch content from any public URL by appending it to the application URL in your web browser or HTTP client. 

### ⏳ Cache Behavior

The application employs a caching system that expires after a preset interval (e.g., 300 seconds). Log outputs in the terminal will inform you whether responses are cache hits or misses.

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework used. 🔥
- [Cachetools](https://cachetools.readthedocs.io/) - Library for caching in Python. ⚡
- [Requests](https://docs.python-requests.org/en/master/) - Simplifies making HTTP requests in Python. 📦
