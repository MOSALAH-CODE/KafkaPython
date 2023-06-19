# Kafka Python

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Overview
This is a sample application built using Kafka and Python. It demonstrates how to use Kafka for message streaming and includes a producer and consumer implementation.

## Features
- Kafka message streaming
- Producer and consumer components
- Dockerized setup with docker-compose

## Prerequisites
- Docker
- Docker Compose

## Installation
1. Clone the repository: `git clone https://github.com/MOSALAH-CODE/KafkaPython.git`
2. Change into the project directory: `cd KafkaPython`
3. Build the Docker containers: `docker-compose build`
4. Start the application: `docker-compose up`

## Usage
Once the application is running, you can access the producer and consumer services using the specified ports. Use the provided Kafka topic to send and receive messages.

## Testing
To test the application, follow these steps:

1. Ensure that the application is running using `docker-compose up`.
2. Open a new terminal window and navigate to the project directory.
3. Run the `InsertData.py` script to add test data to the Kafka topic:
4. `InsertData.py` This script will add sample data to the Kafka topic for testing purposes.

## Contributing
Contributions are welcome! Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License
This project is licensed under the [MIT License](LICENSE).
