pipeline {
  agent any

  environment {
  IMAGE_NAME = '0771637/mongo_spartan:1.' + "$BUILD_NUMBER"
  }

  stages {
    stage('Cloning the project from GitHub'){
      steps {
        git branch: 'main',
        url: 'https://github.com/mrasuli/mongo_spartan.git'
      }
    }

    stage('Build Docker Image') {
      steps{
      script {
        DOCKER_IMAGE = docker.build IMAGE_NAME
      }
      }
    }
    stage("Push to Docker Hub"){
      steps {
        script {
          docker.withRegistry('', 'docker_hub_cred'){
            DOCKER_IMAGE.push()
          }
        }
      }
    }
  }
}
