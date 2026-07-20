#!/bin/bash

# 1. Install Node dependencies and build Tailwind CSS
echo "Building Tailwind CSS..."
npm install
npm run build:css

# 2. Install Python dependencies (This fixes the ImportError!)
echo "Installing Python requirements..."
python3 -m pip install -r requirements.txt

# 3. Run Django collectstatic
echo "Collecting static files..."
python3 manage.py collectstatic --noinput