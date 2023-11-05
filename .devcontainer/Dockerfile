FROM debian:bookworm-slim

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN=true

# preqs
# avoid debconf delaying package configuration, since apt-utils is not installed
RUN apt-get update && \
    apt-get -y install --no-install-recommends apt-utils dialog sudo 2>&1

# Setup User and enable sudo
RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME && \
    chmod 0440 /etc/sudoers.d/$USERNAME

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
        git zsh curl wget nano openssh-client \
        unzip libjpeg-dev libpng-dev libpq-dev \
        # py3
        python3 \
        python3-pip \
        python3-venv \
        python3-wheel \
        python3-setuptools \
        python3-opencv


# Cleanup
RUN apt-get autoremove -fy && \
    apt-get clean && \
    apt-get autoclean -y && \
    rm -rf /var/lib/apt/lists/*

# Use a virtual environment for Python (to avoid PEP668 "externally managed environment" error).
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install Python Packages
RUN pip3 config --user set global.disable-pip-version-check true && \
    pip3 config --user set global.progress_bar off && \
    pip3 config --user set global.no-cache-dir true && \
    pip3 install --upgrade pip && \
    pip3 install --upgrade setuptools && \
    pip3 install --upgrade wheel && \
    pip3 install ipykernel docutils jupyter notebook pyyaml pylint h5py && \
    pip3 install matplotlib seaborn pydotplus && \
    pip3 install scikit-image && \
    pip3 install opencv-python

# re-enable dialog mode for apt-get
ENV DEBIAN_FRONTEND=dialog
