# LocalAI using Docker Compose

To spin up LocalAI using Docker Compose, use the official configuration tailored to your hardware capabilities. Choose
either the CPU setup or the hardware-accelerated Nvidia GPU setup.

## Option 1: CPU Only (Standard Setup)

This setup runs on standard computer processors without any specialized graphics card configurations.

## Option 2: Nvidia GPU Acceleration (Recommended for Speed)

This setup requires the [Nvidia Container Toolkit](https://localai.io/docs/installation/containers/) to leverage CUDA
cores for faster generation speeds.

## How to Launch

1. Create a `models` directory next to your file to persist downloaded weights:
    ```bash
    mkdir models
    ```
2. Start the container in detached (background) mode:
    ```bash
    docker compose up -d
    ```
3. Access the web interface or OpenAI-compatible API endpoint at <http://localhost:8080>. You can check download
   progress using the logs:
    ```bash
    docker compose logs -f
    ```

## Resources

1. LocalAI - <https://localai.io/>
2. Getting Started - <https://localai.io/docs/getting-started/>
3. Docker HUB - <https://hub.docker.com/r/localai/localai>
