FROM ubuntu:22.04

# Set non-interactive mode for apt
ENV DEBIAN_FRONTEND=noninteractive

# Set text encoding
ENV LANG C.UTF-8

# Install essential packages
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    vim \
    python3 \
    python3-pip \
    libpython3-dev \
    wget \
    unzip \
    sudo 

# Create non-privileged account
RUN useradd -ms /bin/bash student -G sudo -p "$(openssl passwd -1 dogfoocatbar)"
USER student

# Tool Directory
RUN mkdir -p ~/tools

# Install OSS CAD Suite
RUN wget -O ~/tools/oss-cad-suite-linux-x64-20250107.tgz https://github.com/YosysHQ/oss-cad-suite-build/releases/download/2025-01-07/oss-cad-suite-linux-x64-20250107.tgz
RUN tar -xzf ~/tools/oss-cad-suite-linux-x64-20250107.tgz -C ~/Utils
RUN rm ~/tools/oss-cad-suite-linux-x64-20250107.tgz
ENV PATH=$PATH:~/tools/oss-cad-suite/bin

# Python Packages
RUN pip install cocotb pytest
