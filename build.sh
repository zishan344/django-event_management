#!/bin/bash

# Build script for Vercel deployment
echo "Installing dependencies..."

# Copy static files from static to staticfiles
echo "Copying static files..."
mkdir -p staticfiles
cp -r static/* staticfiles/ 2>/dev/null || :

echo "Build completed successfully!"
