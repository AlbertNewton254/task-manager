# Deployment Guide

This guide covers multiple deployment options for the Task Manager application.

## Table of Contents
- [Docker Deployment](#docker-deployment)
- [Render Deployment](#render-deployment)
- [Railway Deployment](#railway-deployment)
- [Vercel + Render](#vercel--render)
- [AWS Deployment](#aws-deployment)
- [DigitalOcean](#digitalocean)

---

## Docker Deployment

### Prerequisites
- Docker and Docker Compose installed

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AlbertNewton254/task-manager.git
   cd task-manager
   ```

2. **Build and run with Docker Compose:**
   ```bash
   docker-compose up -d --build
   ```

3. **Access the application:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

4. **Stop the containers:**
   ```bash
   docker-compose down
   ```

### Production Docker

For production, update `docker-compose.yml` environment variables:

```yaml
services:
  backend:
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/taskmanager
      - CORS_ORIGINS=https://yourdomain.com
      - ENVIRONMENT=production
  
  frontend:
    environment:
      - VITE_API_BASE_URL=https://api.yourdomain.com
```

---

## Render Deployment

Render offers free hosting for web services and databases.

### Backend Deployment

1. **Create a new Web Service on Render:**
   - Connect your GitHub repository
   - Root Directory: `backend`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements-prod.txt`
   - Start Command: `gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT`

2. **Add Environment Variables:**
   ```
   DATABASE_URL=sqlite:///./tasks.db
   CORS_ORIGINS=https://your-frontend.onrender.com
   ENVIRONMENT=production
   ```

3. **For PostgreSQL (recommended for production):**
   - Create a PostgreSQL database on Render
   - Use the internal database URL in your environment variables

### Frontend Deployment

1. **Create a new Static Site on Render:**
   - Root Directory: `frontend`
   - Build Command: `npm install && npm run build`
   - Publish Directory: `dist`

2. **Add Environment Variable:**
   ```
   VITE_API_BASE_URL=https://your-backend.onrender.com
   ```

---

## Railway Deployment

Railway provides simple deployment with automatic HTTPS.

### Backend Deployment

1. **Install Railway CLI:**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login and initialize:**
   ```bash
   railway login
   railway init
   ```

3. **Deploy backend:**
   ```bash
   cd backend
   railway up
   ```

4. **Add Environment Variables in Railway Dashboard:**
   ```
   DATABASE_URL=sqlite:///./tasks.db
   CORS_ORIGINS=https://your-frontend.railway.app
   ENVIRONMENT=production
   ```

5. **Set Start Command:**
   ```
   gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
   ```

### Frontend Deployment

1. **Deploy frontend:**
   ```bash
   cd frontend
   railway up
   ```

2. **Add Environment Variable:**
   ```
   VITE_API_BASE_URL=https://your-backend.railway.app
   ```

---

## Vercel + Render

Deploy frontend on Vercel (optimized for React) and backend on Render.

### Frontend on Vercel

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Deploy:**
   ```bash
   cd frontend
   vercel
   ```

3. **Add Environment Variable in Vercel Dashboard:**
   ```
   VITE_API_BASE_URL=https://your-backend.onrender.com
   ```

### Backend on Render

Follow the [Render Backend Deployment](#backend-deployment) steps above.

---

## AWS Deployment

### Using AWS Elastic Beanstalk

#### Backend

1. **Install EB CLI:**
   ```bash
   pip install awsebcli
   ```

2. **Initialize Elastic Beanstalk:**
   ```bash
   cd backend
   eb init -p python-3.11 task-manager-api
   ```

3. **Create environment:**
   ```bash
   eb create task-manager-env
   ```

4. **Set environment variables:**
   ```bash
   eb setenv DATABASE_URL=your-db-url CORS_ORIGINS=your-frontend-url
   ```

5. **Deploy:**
   ```bash
   eb deploy
   ```

#### Frontend (S3 + CloudFront)

1. **Build the frontend:**
   ```bash
   cd frontend
   npm run build
   ```

2. **Create S3 bucket and upload:**
   ```bash
   aws s3 mb s3://task-manager-frontend
   aws s3 sync dist/ s3://task-manager-frontend
   ```

3. **Configure S3 for static website hosting**

4. **Create CloudFront distribution** for HTTPS and CDN

---

## DigitalOcean

### Using App Platform

1. **Create new app on DigitalOcean App Platform**

2. **Connect GitHub repository**

3. **Configure Backend Component:**
   - Type: Web Service
   - Source Directory: `backend`
   - Build Command: `pip install -r requirements-prod.txt`
   - Run Command: `gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080`

4. **Configure Frontend Component:**
   - Type: Static Site
   - Source Directory: `frontend`
   - Build Command: `npm install && npm run build`
   - Output Directory: `dist`

5. **Add Environment Variables**

---

## Post-Deployment Checklist

- [ ] Update CORS origins to include production URLs
- [ ] Set up a production database (PostgreSQL recommended)
- [ ] Configure environment variables
- [ ] Enable HTTPS
- [ ] Set up monitoring and logging
- [ ] Configure backups for database
- [ ] Set up CI/CD pipeline
- [ ] Test all API endpoints
- [ ] Monitor application performance

---

## Database Migration to PostgreSQL

For production, migrate from SQLite to PostgreSQL:

1. **Create PostgreSQL database**

2. **Update DATABASE_URL:**
   ```
   postgresql://username:password@host:5432/database_name
   ```

3. **Install psycopg2:**
   ```bash
   pip install psycopg2-binary
   ```

4. **Run migrations:**
   ```bash
   # Tables will be created automatically on first run
   ```

---

## Monitoring & Logs

### Render
- View logs in Render Dashboard
- Set up log drains to external services

### Railway
- Use Railway CLI: `railway logs`
- View in Railway Dashboard

### AWS
- CloudWatch for logs and metrics
- Set up alarms for critical metrics

---

## Troubleshooting

### CORS Errors
- Ensure frontend URL is in backend CORS_ORIGINS
- Check for trailing slashes in URLs

### Database Connection Issues
- Verify DATABASE_URL format
- Check database service is running
- Ensure network connectivity

### Build Failures
- Check all dependencies are in requirements.txt / package.json
- Verify Node/Python versions match platform requirements
- Review build logs for specific errors

---

## Cost Estimates

| Platform | Free Tier | Paid Plans |
|----------|-----------|------------|
| Render | 750 hours/month | From $7/month |
| Railway | $5 credit/month | Pay as you go |
| Vercel | 100GB bandwidth | From $20/month |
| AWS | 12 months free tier | Variable |
| DigitalOcean | N/A | From $5/month |

---

## Support

For deployment issues, please open an issue on [GitHub](https://github.com/AlbertNewton254/task-manager/issues).
