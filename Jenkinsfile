pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID     = credentials('aws-access-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
        PIP_CACHE_DIR = "${WORKSPACE}\\.pip-cache"
        VENV_DIR = "${WORKSPACE}\\.venv"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                bat '''
                echo Setting up Python virtual environment...
                python -m venv "%VENV_DIR%"
                call "%VENV_DIR%\\Scripts\\activate"
                python -m pip install --upgrade pip
                pip config set global.cache-dir "%PIP_CACHE_DIR%"
                pip install -r requirements.txt dvc[s3]
                '''
            }
        }

        stage('DVC Pull') {
            steps {
                bat '''
                echo Pulling dataset from S3 via DVC...
                call "%VENV_DIR%\\Scripts\\activate"
                dvc pull -r s3remote
                '''
            }
        }

        stage('Run Pipeline') {
            steps {
                bat '''
                echo Running ML pipeline with DVC...
                call "%VENV_DIR%\\Scripts\\activate"
                dvc repro -f
                '''
            }
        }

        stage('Push Artifacts') {
            steps {
                bat '''
                echo Pushing updated artifacts and metrics to S3...
                call "%VENV_DIR%\\Scripts\\activate"
                dvc push -r s3remote
                '''
            }
        }

        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'artifacts/**, metrics/**', fingerprint: true, allowEmptyArchive: true
            }
        }
    }
}
