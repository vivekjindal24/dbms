#!/bin/bash

# Deployment script for Google Cloud Platform
# Usage: ./deploy.sh [cloud-run|app-engine]

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get deployment target
DEPLOY_TARGET=${1:-cloud-run}

echo -e "${GREEN}================================${NC}"
echo -e "${GREEN}DBMS Platform - GCP Deployment${NC}"
echo -e "${GREEN}================================${NC}"
echo ""

# Check if gcloud is installed
if ! command -v gcloud &> /dev/null; then
    echo -e "${RED}Error: gcloud CLI is not installed.${NC}"
    echo "Please install it from: https://cloud.google.com/sdk/docs/install"
    exit 1
fi

# Check if user is authenticated
if ! gcloud auth list --filter=status:ACTIVE --format="value(account)" &> /dev/null; then
    echo -e "${YELLOW}You need to authenticate with Google Cloud.${NC}"
    gcloud auth login
fi

# Get or set project ID
PROJECT_ID=$(gcloud config get-value project 2>/dev/null)
if [ -z "$PROJECT_ID" ]; then
    echo -e "${YELLOW}No project ID set. Please enter your GCP project ID:${NC}"
    read -r PROJECT_ID
    gcloud config set project "$PROJECT_ID"
fi

echo -e "${GREEN}Using project: ${PROJECT_ID}${NC}"
echo ""

# Deploy based on target
case $DEPLOY_TARGET in
    cloud-run)
        echo -e "${GREEN}Deploying to Cloud Run...${NC}"
        echo ""
        
        # Enable required APIs
        echo "Enabling required APIs..."
        gcloud services enable cloudbuild.googleapis.com
        gcloud services enable run.googleapis.com
        gcloud services enable containerregistry.googleapis.com
        
        # Submit build
        echo ""
        echo "Building and deploying container..."
        gcloud builds submit --config=cloudbuild.yaml
        
        # Get service URL
        SERVICE_URL=$(gcloud run services describe dbms-platform --region=us-central1 --format='value(status.url)')
        
        echo ""
        echo -e "${GREEN}================================${NC}"
        echo -e "${GREEN}Deployment Complete!${NC}"
        echo -e "${GREEN}================================${NC}"
        echo ""
        echo -e "${GREEN}Your application is available at:${NC}"
        echo -e "${YELLOW}$SERVICE_URL${NC}"
        echo ""
        ;;
        
    app-engine)
        echo -e "${GREEN}Deploying to App Engine...${NC}"
        echo ""
        
        # Enable App Engine API
        echo "Enabling App Engine API..."
        gcloud services enable appengine.googleapis.com
        
        # Build the application
        echo ""
        echo "Building application..."
        npm run build
        
        # Deploy
        echo ""
        echo "Deploying to App Engine..."
        gcloud app deploy --quiet
        
        # Get service URL
        SERVICE_URL=$(gcloud app browse --no-launch-browser 2>&1 | grep -o 'https://[^[:space:]]*')
        
        echo ""
        echo -e "${GREEN}================================${NC}"
        echo -e "${GREEN}Deployment Complete!${NC}"
        echo -e "${GREEN}================================${NC}"
        echo ""
        echo -e "${GREEN}Your application is available at:${NC}"
        echo -e "${YELLOW}$SERVICE_URL${NC}"
        echo ""
        ;;
        
    *)
        echo -e "${RED}Error: Invalid deployment target.${NC}"
        echo "Usage: ./deploy.sh [cloud-run|app-engine]"
        exit 1
        ;;
esac

echo -e "${YELLOW}Tip: You can view logs with:${NC}"
if [ "$DEPLOY_TARGET" = "cloud-run" ]; then
    echo "  gcloud run logs read --service=dbms-platform --region=us-central1"
else
    echo "  gcloud app logs tail -s default"
fi
echo ""
