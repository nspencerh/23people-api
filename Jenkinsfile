pipeline {

    agent any

    environment {
      HOST = credentials('api-host')
    }

    stages {

      stage('Build') {
        steps {
          sh './scripts/build.sh'
        }
      }

      stage('Push') {
        steps {
          sh './scripts/push.sh'
        }
      }

      stage('Deploy') {
        steps {
          sshagent(credentials : ['23People']) {
            sh 'ssh -o StrictHostKeyChecking=no nicolaspencer@${HOST} uptime'
            sh 'ssh -v nicolaspencer@${HOST}'
            sh "ssh nicolaspencer@${HOST} 'bash -s' < ./scripts/deploy.sh"
          }
        }
      }

    }

}
