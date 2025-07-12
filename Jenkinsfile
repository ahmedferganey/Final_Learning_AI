pipeline {
    agent any

    stages {
        stage('Backend Service') {
            steps {
                dir('07_Computer_Vision/04_EndtoEndProjects/services/backend_service') {
                    echo "🔧 Building backend service..."
                    sh './build.sh'  // or your build commands
                }
            }
        }

        stage('Frontend Service') {
            steps {
                dir('07_Computer_Vision/04_EndtoEndProjects/services/frontend_service') {
                    echo "🎨 Building frontend service..."
                    sh './build.sh'  // or other frontend build steps
                }
            }
        }
    }

    post {
        success {
            echo "✅ All services built successfully."
        }
        failure {
            echo "❌ One or more services failed."
        }
    }
}

