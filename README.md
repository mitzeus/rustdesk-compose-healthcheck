# rustdesk-compose-healthcheck
A simple http healthcheck response for RustDesk's self-hosted docker compose. It checks HBBR &amp; HBBS containers if they are up and returns an OK response, alternatively an error 503 if any of two are down.
