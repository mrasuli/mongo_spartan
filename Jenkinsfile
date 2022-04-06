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

    stage('Build Docker image') {
      steps {
        script {
          DOCKER_IMAGE = docker.build IMAGE_NAME
        }
      }
    }

    stage('Testing the Code') {
      steps{
        script {
          sh '''
            docker run -v $PWD/test-results:/reports --workdir / --rm $IMAGE_NAME pytest -v --junitxml=/reports/results.xml
          '''
          }
        }

        post {
          always {
            junit testResults: '**/test-results/*.xml'
          }
        }
      }

    stage('Push to dockerhub'){
      steps {
        script {
          docker.withRegistry('',DOCKER_CREDENTIALS){
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
