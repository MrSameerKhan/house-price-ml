pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
        }
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python --version
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Application') {
            steps {
                sh '''
                python app.py
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                pytest -v
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded 🎉'
        }
        failure {
            echo 'Pipeline failed ❌'
        }
    }
}
