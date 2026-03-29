# Install with Docker Compose on Windows

Run the following commands in your command line. They work for Windows or Linux systems.

1. Create a directory called loki. Make loki your current working directory:

   ```bash
   mkdir loki
   cd loki
   ```

2. Copy and paste the following commands into your command line to download the `docker-compose.yaml` and `alloy-local-config.yaml` files. If necessary, update the Loki version numbers in the commands to match your version of Loki.

   ```bash
   wget https://raw.githubusercontent.com/grafana/loki/v3.7.0/examples/getting-started/docker-compose.yaml -O docker-compose.yaml
   wget https://raw.githubusercontent.com/grafana/loki/v3.7.0/examples/getting-started/alloy-local-config.yaml -O alloy-local-config.yaml
   wget https://raw.githubusercontent.com/grafana/loki/v3.7.0/examples/getting-started/loki-config.yaml -O loki-config.yaml
   ```

3. With `loki` as the current working directory, run the following `docker-compose` command:

   ```bash
   docker-compose -f docker-compose.yaml up
   ```

   You should see something similar to the following:

   ```bash
   ✔ Container loki-loki-1      Started              0.0s
   ✔ Container loki-grafana-1   Started              0.0s
   ✔ Container loki-alloy-1     Started              0.0s
   ```

4. Verify that Loki is up and running.
   - To view read path readiness, navigate to <http://localhost:3101/ready>.
   - To view read path metrics, navigate to <http://localhost:3101/metrics>.
   - To view write path readiness, navigate to <http://localhost:3102/ready>.
   - To view write path metrics, navigate to <http://localhost:3102/metrics>.

## Resource

**Link -** <https://grafana.com/docs/loki/latest/setup/install/docker/#install-with-docker-compose>
