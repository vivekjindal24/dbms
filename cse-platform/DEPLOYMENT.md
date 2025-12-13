# Deployment Guide - Google Cloud Platform

This guide covers deploying the DBMS Learning Platform to Google Cloud Platform.

## Prerequisites

1. **Google Cloud Account**: Create one at [cloud.google.com](https://cloud.google.com)
2. **gcloud CLI**: Install from [cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install)
3. **Docker** (optional, for local testing): Install from [docker.com](https://www.docker.com/get-started)

## Option 1: Cloud Run (Recommended)

Cloud Run is a serverless container platform that automatically scales your application.

### Benefits
- ✅ Automatic scaling (scales to zero when not in use)
- ✅ Pay only for what you use
- ✅ No server management
- ✅ Built-in load balancing and SSL
- ✅ Fast deployments

### Quick Deploy

```bash
# Make deployment script executable
chmod +x deploy.sh

# Deploy to Cloud Run
./deploy.sh cloud-run
```

### Manual Deployment

```bash
# 1. Authenticate with Google Cloud
gcloud auth login

# 2. Set your project ID
gcloud config set project YOUR_PROJECT_ID

# 3. Enable required APIs
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable containerregistry.googleapis.com

# 4. Build and deploy
gcloud builds submit --config=cloudbuild.yaml

# 5. Your app will be available at the provided URL
```

### Configuration

Edit `cloudbuild.yaml` to customize:
- **Region**: Change `us-central1` to your preferred region
- **Memory**: Adjust `--memory` (default: 512Mi)
- **CPU**: Adjust `--cpu` (default: 1)
- **Max instances**: Adjust `--max-instances` (default: 10)

## Option 2: App Engine

App Engine is a fully managed platform for building scalable web applications.

### Benefits
- ✅ Managed infrastructure
- ✅ Automatic scaling
- ✅ Built-in services (caching, task queues)
- ✅ Multiple versions support
- ✅ Traffic splitting for A/B testing

### Deploy

```bash
# Deploy to App Engine
./deploy.sh app-engine
```

### Manual Deployment

```bash
# 1. Authenticate
gcloud auth login

# 2. Set project
gcloud config set project YOUR_PROJECT_ID

# 3. Enable App Engine
gcloud services enable appengine.googleapis.com

# 4. Build application
npm run build

# 5. Deploy
gcloud app deploy
```

## Local Docker Testing

Test the container locally before deploying:

```bash
# Build the Docker image
docker build -t dbms-platform .

# Run the container
docker run -p 3000:3000 dbms-platform

# Or use Docker Compose
docker-compose up
```

Access at `http://localhost:3000`

## Environment Variables

For production deployments, you can set environment variables:

### Cloud Run
```bash
gcloud run services update dbms-platform \
  --set-env-vars="NODE_ENV=production" \
  --region=us-central1
```

### App Engine
Add to `app.yaml`:
```yaml
env_variables:
  NODE_ENV: 'production'
  CUSTOM_VAR: 'value'
```

## Custom Domain

### Cloud Run
1. Go to Cloud Run console
2. Select your service
3. Click "Manage Custom Domains"
4. Follow the wizard to map your domain

### App Engine
1. Go to App Engine > Settings > Custom Domains
2. Add your domain and verify ownership
3. Update DNS records

## Monitoring and Logs

### View Logs

Cloud Run:
```bash
gcloud run logs read --service=dbms-platform --region=us-central1
```

App Engine:
```bash
gcloud app logs tail -s default
```

### Monitoring

- **Cloud Run**: [console.cloud.google.com/run](https://console.cloud.google.com/run)
- **App Engine**: [console.cloud.google.com/appengine](https://console.cloud.google.com/appengine)
- **Cloud Monitoring**: [console.cloud.google.com/monitoring](https://console.cloud.google.com/monitoring)

## Cost Optimization

### Cloud Run (Free Tier)
- 2 million requests/month
- 360,000 GB-seconds memory
- 180,000 vCPU-seconds

### Tips
1. **Use auto-scaling**: Scale to 0 when not in use
2. **Optimize image size**: Use multi-stage Docker builds (already configured)
3. **Enable caching**: Use CDN for static assets
4. **Monitor usage**: Set up billing alerts

## Troubleshooting

### Build Fails
```bash
# Check build logs
gcloud builds list
gcloud builds log <BUILD_ID>
```

### Service Not Starting
```bash
# Check service logs
gcloud run logs read --service=dbms-platform --region=us-central1 --limit=50
```

### Out of Memory
Increase memory allocation in `cloudbuild.yaml`:
```yaml
--memory '1Gi'
```

## CI/CD Setup

### GitHub Actions

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Cloud Run

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - uses: google-github-actions/setup-gcloud@v1
        with:
          service_account_key: ${{ secrets.GCP_SA_KEY }}
          project_id: ${{ secrets.GCP_PROJECT_ID }}
      
      - name: Deploy
        run: gcloud builds submit --config=cloudbuild.yaml
```

### GitLab CI/CD

Create `.gitlab-ci.yml`:

```yaml
deploy:
  image: google/cloud-sdk:alpine
  stage: deploy
  script:
    - echo $GCP_SA_KEY | base64 -d > ${HOME}/gcp-key.json
    - gcloud auth activate-service-account --key-file ${HOME}/gcp-key.json
    - gcloud config set project $GCP_PROJECT_ID
    - gcloud builds submit --config=cloudbuild.yaml
  only:
    - main
```

## Security Best Practices

1. **Use HTTPS**: Cloud Run and App Engine provide automatic HTTPS
2. **Least privilege**: Use service accounts with minimal permissions
3. **Secrets management**: Use Secret Manager for sensitive data
4. **Regular updates**: Keep dependencies updated
5. **Enable audit logging**: Track access and changes

## Support

- **GCP Documentation**: [cloud.google.com/docs](https://cloud.google.com/docs)
- **Cloud Run**: [cloud.google.com/run/docs](https://cloud.google.com/run/docs)
- **App Engine**: [cloud.google.com/appengine/docs](https://cloud.google.com/appengine/docs)

## Next Steps

1. Deploy your application
2. Set up custom domain
3. Configure monitoring and alerts
4. Set up CI/CD pipeline
5. Implement caching strategy
6. Add error tracking (e.g., Sentry)
