# [ FASPO ] Batch-Data Service

This repository contains source code for the _Batch-Data Service_ in FASPO concept project. The _Batch-Data Service_ is 
a part of much larger system that is utilizing microservices architecture. It's main responsibility is to download 
large datasets from external sources and transform them into an internal format. In the context of Czech Republic it
retrieves batches of financial data from the [https://monitor.statnipokladna.cz/](Ministry of Finance).

## Prerequisites

* Python 3.11 or higher
* packages listed in `requirements.txt`

## Environment Variables

* `DATA_SOURCE_URL`: URL of the external data source (default: `https://monitor.statnipokladna.cz/data/extrakty/csv`)
* `DATA_TARGET_URL`: URL of the internal data target, i.e. Store Service HOST
* `SCHEDULE_HOUR`: Hour of the day when automatic check runs (default: `0`)
* `SCHEDULE_MINUTE`: Minute of the hour when automatic check runs (default: `0`)
* `LOG_INFO`: Log level for info messages (default: `INFO`)

## Installation (Direct)

1. Make sure Python 3.11 is installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory.
4. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```
5. Activate the virtual environment:
    ```bash
     source venv/bin/activate
     ```
6. Install the required packages:
7. ```bash
   pip install -r requirements.txt
   ```
9. Run the application:
   ```bash
   python main.py
   ```
   or
   ```bash
   uvicorn main:app --host <your_host> --port <your_port>
   ```
10. The application should now be running and accessible at `http://0.0.0.0:8080`.

## Installation (Docker)

1. Make sure Docker is installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory.
4. Build the Docker image:
   ```bash
   docker build -t batch-data-service .
   ```
5. Run the Docker container:
   ```bash
    docker run -d -p 8080:8080 --env <ENV_NAME>=<ENV_VALUE> -- batch-data-service
    ```
