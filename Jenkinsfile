pipeline {
    
    agent any

    triggers {
        pollSCM('')
    }

    stages {
        
        stage('Install') {
            steps {
                sh 'echo "installing the required dependencies in requirements.txt using pip"'
                sh 'pip install -r requirements.txt --user'
            }
        }

        stage('Test') {
            steps {
                sh 'echo "executing tests using pytest"'
                sh 'python -m pytest --html=reports/flask-test-report.html --self-contained-html test_app.py'
            }
        }

        stage('Build') {
            steps {
                sh 'echo "building the repo"'
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                sh "docker build -t flaskapp:${env.BUILD_ID} ."
                sh "docker images"
            }
        }

        stage('Docker Delete Container') {
            steps {
                echo 'Delete existing container if any'
                sh 'docker ps -qa --filter "name=flaskdemo" | xargs -r docker rm -f'                
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the flask test application'
                sh "docker run -itd -p 8070:5000 --name=flaskdemo flaskapp:${env.BUILD_ID}"
                sh 'docker ps -a'
            }
        }
    }

    post {
        always {
            echo 'The pipeline completed, publishing results as report'
            // publish html
            publishHTML target: [
                allowMissing: false,
                alwaysLinkToLastBuild: false,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'flask-test-report.html',
                reportName: 'Flask Test Results'
            ]
        }
        success {
            echo 'Flask Application Up and running!!'
        }
        failure {
            echo 'Build stage failed'
            error('Stopping early…')
        }
    }
}
