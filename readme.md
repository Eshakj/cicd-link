# Simple Python Flask Web Application with CI/CD

This project demonstrates a basic Continuous Integration and Continuous Delivery (CI/CD) pipeline using GitHub Actions for a simple Python web application built with Flask.

## Project Overview

The Python web application is a minimal Flask app that defines two routes:

* `/`: Returns a "Hello, World!" message.
* `/greet/<name>`: Returns a personalized greeting "Hello, [name]!".

The CI/CD pipeline automates the following stages upon code changes pushed to the `main` branch or when a pull request is made against it:

* **Build:** Sets up the Python environment and installs the necessary dependencies (currently just Flask, as specified in `requirements.txt`).
* **Deploy:** A simplified step that simulates the deployment process by printing messages to the GitHub Actions logs. In a real-world scenario, this step would involve deploying the application to a hosting platform.
* **Notify:** A basic notification that prints a success message to the GitHub Actions logs after the "deployment" step.

## CI/CD Pipeline

The CI/CD pipeline is defined in the `.github/workflows/ci.yml` file and uses GitHub Actions. The workflow consists of three jobs:

* **`build`**:
    * Checks out the code.
    * Sets up the Python environment.
    * Installs dependencies from `requirements.txt`.
* **`deploy`**:
    * Runs only after the `build` job has completed successfully (`needs: build`).
    * Prints messages simulating the deployment process.
* **`notify`**:
    * Runs only after the `deploy` job has completed successfully (`needs: deploy`).
    * Prints a message indicating successful "deployment."

## Getting Started

To run this project locally:

1.  **Clone the repository:**
    ```bash
    git clone [your-repository-url]
    cd [your-repository-name]
    ```
2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate   # On Windows
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Flask application:**
    ```bash
    python app.py
    ```
5.  **Open your web browser and navigate to `http://localhost:5000/`** to see the "Hello, World!" message. You can also try `http://localhost:5000/greet/YourName`.

## Files in the Repository

* `app.py`: Contains the Flask web application code.
* `requirements.txt`: Lists the project dependencies (currently Flask).
* `.github/workflows/ci.yml`: Defines the GitHub Actions CI/CD pipeline.
* `README.md`: This file, providing information about the project.

## Contributing

Feel free to fork this repository and contribute by adding more features, tests, or improvements to the CI/CD pipeline.

