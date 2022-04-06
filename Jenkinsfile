pipeline {
  agent any

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
        DOCKER_IMAGE = docker.build '0771637/mongo_spartan'
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
