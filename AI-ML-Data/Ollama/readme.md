# Local AI Stack via Docker Compose

For a completely container-native workflow, pair Ollama (the inference engine) with Open WebUI (the front-end interface)
using a single docker compose.

There are two options to run Ollama locally,

1. With Nvidia GPU
2. CPU only

## Deployment Steps

```bash
# Start the stack
docker compose up -d

# Download a model into the Ollama container (e.g., Llama 3.2)
docker exec -it ollama ollama run llama3.2
```

Once deployed, navigate to <http://localhost:3000> in your web browser to open the UI chat room.

## Resources

* Run AI Models Locally - <https://www.docker.com/products/model-runner/>
* WebUI - <https://www.docker.com/blog/open-webui-docker-desktop-model-runner/>
