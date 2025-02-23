pipeline {
    agent any
    environment {
        // Reference the credential by its ID
        GITHUB_TOKEN = credentials('Github')
    }
    stages {
        stage('Test Webhook') {
            steps {
                echo 'Webhook triggered successfully!'
                echo 'GitHub Token is being used, but no Git operations are performed.'
            }
        }
    }
}