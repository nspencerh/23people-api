pipeline {

    agent any

    environment {
      api-host = credentials('api-host')
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
                sh 'ssh -o StrictHostKeyChecking=no nicolaspencer@35.184.120.48 uptime'
                sh 'ssh -v nicolaspencer@$api-host'
                sh './scripts/deploy.sh'
              }
            }
        }
    }
}
