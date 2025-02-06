# Use a Python image with Node.js pre-installed for frontend needs
FROM nikolaik/python-nodejs:latest

# Update package lists and install required tools
RUN apt-get update && apt-get upgrade -y
RUN apt-get -y install fish git sudo

# Define arguments for creating a non-root user
ARG USERNAME=dev
ARG USER_UID=1001
ARG USER_GID=$USER_UID

# Create a new user with sudo privileges
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME -p "" \
    && adduser $USERNAME sudo

# Set working directory
WORKDIR /workspace

# Switch to non-root user
USER $USERNAME
