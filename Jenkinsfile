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
        docker.build '0771637/mongo_spartan'
      }
      }
    }
  }
}
