# Activity 7: the image the workflow builds and runs.
FROM python:3.9-slim

WORKDIR /app

# Git lets update_index.sh commit and push. Perl ships with this image.
RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

# Copy the whole repository (including .git) into the image.
COPY . /app

RUN chmod +x /app/.github/scripts/entrypoint.sh /app/.github/scripts/update_index.sh

ENTRYPOINT ["/app/.github/scripts/entrypoint.sh"]
