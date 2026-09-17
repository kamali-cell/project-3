pipeline {
    agent any
    environment {
        // Defining custom variables for your Online Exam system
        EXAM_APP_NAME = 'Online_Exam_Evaluation_System'
        EXAM_APP_VERSION = '1.0.0'
    }
    stages {
        stage('Checkout Source Code') {
            steps {
                // Downloads your files from GitHub into Jenkins
                checkout scm
            }
        }
        stage('Display Application Info') {
            steps {
                // Uses the custom environment variables to print info
                echo "Initializing deployment for ${env.EXAM_APP_NAME}"
                echo "Current System Version: ${env.EXAM_APP_VERSION}"
            }
        }
        stage('Compile Application Code') {
            steps {
                // Compiles the python code to check for syntax errors
                bat 'python -m py_compile app.py'
                echo "Success: ${env.EXAM_APP_NAME} version ${env.EXAM_APP_VERSION} compiled perfectly."
            }
        }
    }
}
