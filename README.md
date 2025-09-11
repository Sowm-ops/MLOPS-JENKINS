# Jenkins MLOps Pipeline with DVC + S3

This repository contains an end-to-end CI/CD pipeline for ML workflows using:
- **DVC** for dataset + artifact versioning
- **S3** as the remote storage
- **Jenkins** for orchestration

### Steps
1. Clone repo
2. Setup DVC and S3 remote
3. Run pipeline locally:
   ```bash
   dvc repro
   dvc push -r s3remote
   ```
4. Configure Jenkins with AWS credentials and run the Jenkinsfile pipeline
