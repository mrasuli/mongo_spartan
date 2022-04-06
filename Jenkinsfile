pipeline {
  agent any

  environment {
  IMAGE_NAME = '0771637/mongo_spartan:1.' + "$BUILD_NUMBER"
  DOCKER_CREDNETIALS = "docker_hub_cred"
  }

  stages {
  stage('Cloning the project from GitHub'){
    steps {
      checkout([
          $class: 'GitSCM', branches: [[name: '*/main']],
          serRemoteConfigs: [[
            url: 'git@github.com:mrasuli/mongo_spartan.git',
            credentialsId: 'ssh_git_cred'
          ]]
        ])
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
    stage('Removing the Docker Image'){
      steps {
        sh "docker rmi $IMAGE_NAME"
      }
    }
  }
}
