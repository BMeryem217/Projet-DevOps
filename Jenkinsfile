pipeline {
    agent any
    environment {
        // Reference the GitHub token credential by its ID
        GITHUB_TOKEN = credentials('Github')
        // Docker image name and tag
        DOCKER_IMAGE_NAME = 'meryembounit/devops'
        BUILD_TAG = "${env.BUILD_ID}" // Use Jenkins build ID as the tag
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh """
                        echo "Listing workspace directory:"
                        ls -l ${WORKSPACE}
                        echo "Building Docker image..."
                        docker build -f ${WORKSPACE}/Dockerfile -t ${DOCKER_IMAGE_NAME}:${BUILD_TAG} -t ${DOCKER_IMAGE_NAME}:latest ${WORKSPACE}
                    """
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    script {
                        sh """
                            echo \$PASSWORD | docker login -u \$USERNAME --password-stdin
                            docker push ${DOCKER_IMAGE_NAME}:${BUILD_TAG}
                            docker push ${DOCKER_IMAGE_NAME}:latest
                        """
                    }
                }
            }
        }
    }
}