pipeline {

    agent any

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
            sh 'ssh -o StrictHostKeyChecking=no nicolaspencer@35.239.202.208 uptime'
            sh 'ssh -v nicolaspencer@35.239.202.208'
            sh './scripts/deploy.sh'
          }
        }
      }

    }

}
