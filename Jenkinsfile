pipeline {
  agent any

  environment {
    AWS_ACCESS_KEY_ID     = credentials('aws-access-key-id')
    AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
    PIP_CACHE_DIR = "${WORKSPACE}/.pip-cache"
    VENV_DIR = "${WORKSPACE}/.venv"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Setup Environment') {
      steps {
        sh '''
          python3 -m venv "${VENV_DIR}"
          . "${VENV_DIR}/bin/activate"
          python -m pip install --upgrade pip
          pip config set global.cache-dir "${PIP_CACHE_DIR}"
          pip install -r requirements.txt
        '''
      }
    }

    stage('DVC Pull') {
      steps {
        sh '''
          . "${VENV_DIR}/bin/activate"
          dvc pull -r s3remote
        '''
      }
    }

    stage('Run Pipeline') {
      steps {
        sh '''
          . "${VENV_DIR}/bin/activate"
          dvc repro -f
        '''
      }
    }

    stage('Push Artifacts') {
      steps {
        sh '''
          . "${VENV_DIR}/bin/activate"
          dvc push -r s3remote
        '''
      }
    }

    stage('Archive Results') {
      steps {
        archiveArtifacts artifacts: 'artifacts/** metrics/**', fingerprint: true, allowEmptyArchive: true
      }
    }
  }
}
