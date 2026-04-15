# 3. Preparation (The "Manjaro Move")

Since Docker containers run with specific permissions, you should create the directory and set the ownership before spinning up the container. Run these commands in your terminal:

```bash
# 1. Create the directory structure in your home
mkdir -p ~/neo4j_storage/{data,logs,import,plugins}

# 2. Ensure your user owns it (replace 1000 with your actual ID if different)
sudo chown -R 1000:1000 ~/neo4j_storage

# 3. Navigate to your AiQL project and fire it up
docker-compose up -d
```
