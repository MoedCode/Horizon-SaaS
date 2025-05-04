#!/bin/bash

REQUIRED_PYTHON="3.11.11"
REQUIRED_PIP="24.0"

# Function to compare versions
version_lt() {
  [ "$(printf '%s\n' "$1" "$2" | sort -V | head -n1)" != "$2" ]
}

# Check Python
if command -v python3 &>/dev/null; then
    INSTALLED_PYTHON=$(python3 --version | awk '{print $2}')
    echo "Python found: $INSTALLED_PYTHON"

    if version_lt "$INSTALLED_PYTHON" "$REQUIRED_PYTHON"; then
        echo "Python version is lower than required ($REQUIRED_PYTHON)."
        read -p "Install Python $REQUIRED_PYTHON? [y/n]: " choice
        if [[ "$choice" == "y" ]]; then
            echo "Installing Python $REQUIRED_PYTHON..."
            # Add your installation commands here (platform-dependent)
        else
            echo "Exiting setup."
            exit 1
        fi
    else
        echo "Python version is OK."
    fi
else
    echo "Python is not installed. Installing Python $REQUIRED_PYTHON..."
    # Add installation command here
fi

# Check pip
if command -v pip3 &>/dev/null; then
    INSTALLED_PIP=$(pip3 --version | awk '{print $2}')
    echo "pip found: $INSTALLED_PIP"

    if version_lt "$INSTALLED_PIP" "$REQUIRED_PIP"; then
        echo "pip version is lower than required ($REQUIRED_PIP)."
        read -p "Upgrade pip to $REQUIRED_PIP? [y/n]: " choice
        if [[ "$choice" == "y" ]]; then
            python3 -m pip install --upgrade pip
        else
            echo "Exiting setup."
            exit 1
        fi
    else
        echo "pip version is OK."
    fi
else
    echo "pip is not installed. Installing pip..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py
fi

echo "✅ Environment check complete."
