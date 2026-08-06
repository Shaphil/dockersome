# ClickHouse Single Node with Docker Compose

To run ClickHouse using Docker Compose, create a `compose.yml` file to spin up a single-node instance.

## Important Setup Steps

1. **Fix File Permissions:** ClickHouse containers run by default using user/group ID `101:101`. Create the local
   directory structure and assign ownership to avoid immediate container crashes or permission errors:
    ```bash
    mkdir ch_data ch_logs
    sudo chown -R 101:101 ch_data ch_logs
    ```
2. **Start the Container:** Run this standard command to pull the official image and start ClickHouse in background
   mode:
    ```bash
    docker compose up -d
    ```
3. **Verify the Installation:** Use the standard built-in client utility inside the running container to execute a test
   query:
    ```bash
    docker compose exec clickhouse clickhouse-client --query "SELECT 1"
    ```

## Connecting to ClickHouse

* **Database Client:** Connect your favorite SQL IDE (like DBeaver or DataGrip) via native TCP on port `9000`.
* **Web UI / Applications:** Connect HTTP applications via port `8123`.
* **Credentials:** The default configuration creates an administrative user named `default` with **no password**. For a
  secure setup, you can check
  the [Official ClickHouse Documentation](https://clickhouse.com/docs/get-started/setup/self-managed/docker) to mount a
  customized user definition XML file.

## Resources

* ClickHouse Docs - <https://clickhouse.com/docs>
* Set Up ClickHouse with Docker Compose - <https://last9.io/blog/set-up-clickhouse-with-docker-compose/>
