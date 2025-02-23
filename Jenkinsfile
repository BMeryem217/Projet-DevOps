pipeline {
    agent any
    environment {
        // Reference the credential by its ID
        GITHUB_TOKEN = credentials('Github')
    }
    stages {
        stage('Clone Repository') {
            steps {
                sh '''
                    // Use the token in the Git URL
                    git clone https://${GITHUB_TOKEN}@github.com/BMeryem217/Projet-DevOps.git
                '''
            }
        }
    }
}