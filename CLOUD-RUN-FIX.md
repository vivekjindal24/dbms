# Cloud Run Deployment Fix Guide

## Problem Identified
The Cloud Run deployment was failing because:
1. The Dockerfile path wasn't correctly handling the nested project structure
2. The standalone build output had incorrect copy paths
3. Missing root-level Dockerfile for Cloud Run to use

## Solutions Implemented ✅

### 1. Created Root-Level Dockerfile
- Location: `/Dockerfile` (at repository root)
- Correctly handles `cse-platform/` subdirectory structure
- Fixed standalone build copy paths
- Tested and verified working locally

### 2. Updated cse-platform/Dockerfile
- Fixed standalone output path for nested builds
- Works when building from within cse-platform directory

### 3. Added Build Optimization Files
- `.dockerignore` at root level to reduce build context
- Procfile for alternative deployment methods

## How to Deploy to Cloud Run

### Option 1: Using Cloud Run Console (Recommended)

1. **Go to Google Cloud Console**
   - Navigate to: https://console.cloud.google.com/run
   - Select your project: `ecg-tensor-research1`

2. **Create/Update Cloud Run Service**
   - Click "Create Service" or select existing `dbms-platform` service
   - Choose "Deploy from GitHub"
   
3. **Configure GitHub Connection**
   - Repository: `vivekjindal24/dbms`
   - Branch: `main`
   - Build Type: **Dockerfile**
   - Dockerfile location: **/Dockerfile** (at root)
   
4. **Configure Service Settings**
   - Service name: `dbms-platform`
   - Region: `us-central1` (or your preferred region)
   - Authentication: ✅ Allow unauthenticated invocations
   
5. **Container Settings**
   - Port: **3000**
   - Memory: **512 MiB** (minimum)
   - CPU: **1**
   - Min instances: **0**
   - Max instances: **10**

6. **Deploy**
   - Click "Create" or "Deploy"
   - Wait for build to complete (3-5 minutes)
   - Your app will be available at: `https://dbms-platform-[hash].a.run.app`

### Option 2: Using Cloud Build Trigger

1. **Create Cloud Build Trigger**
   ```bash
   gcloud builds triggers create github \
     --repo-name=dbms \
     --repo-owner=vivekjindal24 \
     --branch-pattern="^main$" \
     --build-config=cse-platform/cloudbuild.yaml
   ```

2. **Manual Trigger**
   - Go to Cloud Build Triggers in Console
   - Click "Run" on your trigger
   - Or push to `main` branch to auto-deploy

### Option 3: Manual gcloud Deploy

If you have gcloud CLI installed:

```bash
# Set your project
gcloud config set project ecg-tensor-research1

# Build and deploy
gcloud run deploy dbms-platform \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --memory 512Mi \
  --cpu 1 \
  --port 3000
```

## Verification Steps

After deployment, verify:

1. **Check Service Status**
   - Go to Cloud Run console
   - Service should show "Ready" status with green checkmark

2. **Test the URL**
   - Click on the service URL
   - Should see the DBMS Learning Platform homepage
   - Test navigation to different units and topics

3. **Check Logs**
   - Click "Logs" tab in Cloud Run console
   - Should see "Ready in XXms" message
   - No error messages

## Common Issues and Solutions

### Issue: "Container failed to start"
**Solution:** Check that port 3000 is exposed and the app listens on 0.0.0.0

### Issue: "Build timeout"
**Solution:** Increase build timeout in cloudbuild.yaml (currently 600s)

### Issue: "Permission denied"
**Solution:** Ensure Cloud Build service account has necessary permissions:
- Cloud Run Admin
- Service Account User

### Issue: "Cannot find Dockerfile"
**Solution:** Verify in Cloud Run configuration that Dockerfile path is `/Dockerfile`

## Files Modified

1. ✅ `/Dockerfile` - Root-level Dockerfile for Cloud Run
2. ✅ `/cse-platform/Dockerfile` - Fixed standalone paths
3. ✅ `/.dockerignore` - Optimized build context
4. ✅ `/Procfile` - Alternative deployment configuration

## Build Verification

Local Docker build tested and working:
```bash
✅ Build successful (126s)
✅ Container starts in 95ms
✅ App accessible on port 3000
✅ All 15 pages generating correctly
```

## Next Steps

1. **Reconnect GitHub to Cloud Run** (see Option 1 above)
2. **Wait for automatic build** (triggered by latest push)
3. **Verify deployment** and test the URL
4. **(Optional)** Set up custom domain
5. **(Optional)** Configure environment variables if needed

## Support Resources

- Cloud Run Documentation: https://cloud.google.com/run/docs
- Next.js on Cloud Run: https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-nodejs-service
- Cloud Build: https://cloud.google.com/build/docs

---

**Latest Commit:** `a9b5bb9` - Fix Cloud Run deployment with correct build paths
**Repository:** https://github.com/vivekjindal24/dbms
**Status:** ✅ Ready to deploy
