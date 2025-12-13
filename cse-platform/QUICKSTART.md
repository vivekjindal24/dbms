# Quick Start - Google Cloud Deployment

## 🚀 Deploy in 3 Steps

### Step 1: Authenticate with Google Cloud

```bash
# Install gcloud CLI if you haven't already
# macOS: brew install --cask google-cloud-sdk
# Windows: Download from https://cloud.google.com/sdk/docs/install

# Login to your Google account
gcloud auth login

# Set your project (create one at console.cloud.google.com if needed)
gcloud config set project YOUR_PROJECT_ID
```

### Step 2: Make Deployment Script Executable

```bash
cd cse-platform
chmod +x deploy.sh
```

### Step 3: Deploy!

```bash
# Deploy to Cloud Run (Recommended - Free tier available)
./deploy.sh cloud-run

# OR deploy to App Engine
./deploy.sh app-engine
```

That's it! Your application will be live in ~3-5 minutes. 🎉

---

## 🐳 Local Docker Testing (Optional)

Test the container locally before deploying:

```bash
# Build the image
docker build -t dbms-platform .

# Run the container
docker run -p 3000:3000 dbms-platform

# Access at http://localhost:3000
```

Or use Docker Compose:

```bash
docker-compose up
```

---

## 💰 Cost Estimate

### Cloud Run (Pay-as-you-go)
- **Free Tier**: 2 million requests/month
- **Estimated Cost**: $0-5/month for small to medium traffic
- **Best For**: Development, small projects, variable traffic

### App Engine (Pay-as-you-go)
- **Free Tier**: 28 instance hours/day
- **Estimated Cost**: $5-20/month for consistent traffic
- **Best For**: Production apps with steady traffic

---

## 📊 What Gets Deployed

Your deployment includes:
- ✅ Optimized Next.js production build
- ✅ Multi-stage Docker container (minimal size)
- ✅ Automatic HTTPS and SSL certificates
- ✅ Auto-scaling (scales to zero when not in use)
- ✅ Built-in load balancing
- ✅ Cloud logging and monitoring

---

## 🔧 Troubleshooting

### "gcloud: command not found"
Install Google Cloud SDK: https://cloud.google.com/sdk/docs/install

### "Docker daemon is not running"
Start Docker Desktop on your machine

### "Permission denied"
Run: `chmod +x deploy.sh`

### Need help?
See detailed documentation in `DEPLOYMENT.md`

---

## 📱 Access Your App

After deployment completes, you'll see:

```
================================
Deployment Complete!
================================

Your application is available at:
https://dbms-platform-xxxxx-uc.a.run.app
```

Click the link to view your live application!

---

## 🎯 Next Steps

1. ✅ Deploy your app
2. 🌐 Set up custom domain (optional)
3. 📈 Configure monitoring alerts
4. 🔄 Set up CI/CD for automatic deployments
5. 🔐 Add environment variables for sensitive data

See `DEPLOYMENT.md` for detailed instructions on each step.
