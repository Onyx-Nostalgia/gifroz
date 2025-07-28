#!/bin/bash

# A script to add Python dependencies using uv and update requirements.txt

# Exit immediately if a command exits with a non-zero status.
set -e

# Check if at least one library is provided as an argument.
if [ $# -eq 0 ]; then
    echo "Usage: $0 <library1> [library2] ... [\"library3>=1.0.0\"]" >&2
    echo "Error: No libraries specified." >&2
    exit 1
fi

echo "Adding the following libraries to pyproject.toml: $@"
uv add "$@"

echo "Compiling pyproject.toml to requirements.txt..."
uv pip compile pyproject.toml -o requirements.txt

echo "✅ Successfully added libraries and updated requirements.txt."

