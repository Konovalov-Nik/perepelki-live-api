FROM resin/rpi-raspbian

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python \
    python-dev \
    python-pip \
    python-virtualenv \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Define working directory
WORKDIR /data

COPY ./* ./

RUN pip install -r requirements.txt

RUN pip install .

EXPOSE 5000/tcp