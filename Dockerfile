FROM python:3.7-slim

WORKDIR /opt/python-bad-project

# Install dependencies
RUN apt-get update && apt-get install -y \
    iputils-ping \
    curl

# Install uv and add to PATH
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"

# Copy project files
COPY . .

# Install dependencies using uv
RUN uv venv --python 3.7
RUN . .venv/bin/activate && \
    uv pip install -e '.[dev]'

