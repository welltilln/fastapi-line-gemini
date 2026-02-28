#!/bin/bash

# Clear port 8000 if it's already in use to prevent collision
lsof -ti:8000 | xargs kill -9 &>/dev/null || true

# Activate virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo " Error: venv not found. Please setup first."
    exit 1
fi

# Run the app with maximum silence and OCD-friendly output
# Suppressing all Python and Google-specific deprecation warnings
export PYTHONWARNINGS="ignore"
export GRPC_VERBOSITY="NONE"

echo "============================================================"
echo " YOSAFE SILENT INPUT ENGINE (Modern Hub)"
echo "============================================================"

# Using the local venv python which is now 3.10.19
python -m app.main
 