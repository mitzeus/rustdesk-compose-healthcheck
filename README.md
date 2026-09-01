# RustDesk Compose Healthcheck

A simple http healthcheck response for RustDesk's self-hosted docker compose. It checks HBBR &amp; HBBS containers if they are up and returns an OK response, alternatively an error 503 if any of two are down.

## Setup

### 1. Add another service in RustDesk's `docker-compose.yml` file:

```yaml
services:
  hbbs: ...

  hbbr: ...

  rustdesk-health:
    container_name: rustdesk-health
    image: mitzeus/rustdesk-healthcheck
    ports:
      - "22116:22116/tcp"
    networks:
      - rustdesk
    restart: unless-stopped
```

### 2. Add all services to a shared network:

```yaml
services:
    hbbs:
    ...
    networks:
        - rustdesk
    ...

    hbbr:
    ...
    networks:
        - rustdesk
    ...

    rustdesk-health:
    ...
    networks:
        - rustdesk
    ...

networks:
    rustdesk:
```

### 3. Remove RustDesk `hbbr` & `hbbs` network mode from host and declare appropriate ports:

```yaml
services:
    hbbs:
    ...
    # network_mode: "host" # comment this out
    ports:
      - "21115:21115/tcp"
      - "21116:21116/tcp"
      - "21116:21116/udp"
      - "21118:21118/tcp"
    ...

    hbbr:
    ...
    # network_mode: "host" # comment this out
    ports:
      - "21117:21117/tcp"
      - "21119:21119/tcp"
    ...

    rustdesk-health:
    ...
    ports:
      - "22116:22116/tcp"
    ...

networks:
    rustdesk:
```

As RustDesk uses these ports as default, they should follow this setup above. Depending on your setup or changes in RustDesk's usage of ports (for example differing setups between the OSS & Pro versions) this could change. [Read the RustDesk documentation about Self-Hosting.](https://rustdesk.com/docs/en/self-host/rustdesk-server-oss/docker/)

### 4. Test the setup

When running the container is running, the http response should be open at http://{host_local_ip}:22116/health. The response should now be either `"OK"`, or return an error 503 with `{ hbbr: {true/false}, hbbs: {true/false} }`.

## Usage

One usage is to be able to ping RustDesk status in a dashboard such as [Homarr](https://homarr.dev/) by creating a new RustDesk app, and add http://{host_local_ip}:22116/health as the ping. It should then show green if the response is `"OK"` and show red otherwise.
