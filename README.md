# Docker Demo

## Local Development Setup

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Update `.env` with your credentials

3. Run:
   ```bash
   docker-compose up --build
   ```

## CI/CD Setup (GitHub Actions)

No `.env` file needed! Add these secrets in GitHub repository settings (Settings → Secrets → Actions):

### Database Secrets
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`

### SonarQube Secrets
- `SONAR_TOKEN` - Get from https://sonarcloud.io
- `SONAR_HOST_URL` - Set to `https://sonarcloud.io`

### Docker Hub Secrets
- `DOCKER_USERNAME` - Your Docker Hub username
- `DOCKER_PASSWORD` - Docker Hub access token (create at https://hub.docker.com/settings/security)

### SonarCloud Setup
1. Sign in to https://sonarcloud.io with GitHub
2. Import your repository
3. Update `sonar-project.properties` with your projectKey and organization

### Pipeline Features
- ✅ Code quality analysis (SonarQube)
- ✅ Container vulnerability scanning (Trivy)
- ✅ Automated Docker builds
- ✅ Docker Hub image publishing
- ✅ Security alerts in GitHub Security tab

Secrets are passed directly to docker-compose as environment variables in the workflow.

### Get Latest Action SHA
To get the latest commit SHA for GitHub Actions:
```bash
git ls-remote https://github.com/sonarsource/sonarqube-quality-gate-action.git HEAD | awk '{print $1}'
```

## Git Commands

### Push changes to repository
```bash
git add .
git commit -m "Your commit message"
git push origin main
```

### Create and push a tag
```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

### Push all tags
```bash
git push origin --tags
```


# hey this is new