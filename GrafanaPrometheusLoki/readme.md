# PLG Stack (Prometheus, Loki, and Grafana)

Setting up the PLG Stack (Prometheus, Loki, and Grafana) with Docker Compose is a common way to create a local observability environment for monitoring metrics and logs.

## Core Stack Components

- **[Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/)**: The visualization layer used to build dashboards and query both metrics and logs.
- **[Prometheus](https://prometheus.io/docs/guides/cadvisor/#docker-compose-configuration)**: The time-series database that collects and stores metrics.
- **[Loki](https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/)**: The log aggregation system that stores and indexes logs.
- **[Grafana Alloy](https://grafana.com/docs/alloy/latest/) or Promtail**: The agents responsible for scraping logs (from files or Docker) and shipping them to Loki.

## Quickstart Resources

- **Official Quickstart:** Grafana Labs provides a pre-configured repository that you can clone and run with `docker compose up -d` to see the stack in action immediately.
- **Loki Installation:** For detailed instructions on running Loki specifically, refer to the official Docker Compose guide.
- **Complete Observability Guide:** A comprehensive guide on setting up the full stack, including [Tempo](https://grafana.com/oss/loki/) for traces, can be found on [OneUptime](https://oneuptime.com/blog/post/2026-02-06-docker-compose-observability-stack/view).

## Implementation Tips

- **Default Credentials:** For a fresh Grafana installation, the default username and password are both admin.
- **Data Sources:** Once the containers are running, you must add Prometheus (`http://prometheus:9090`) and Loki (`http://loki:3100`) as data sources within the Grafana UI.
- **Permissions:** Loki containers often run as a non-root user (UID 10001), so ensure your mounted volumes have the [correct permissions](https://github.com/grafana/loki/blob/main/production/docker/docker-compose.yaml).
