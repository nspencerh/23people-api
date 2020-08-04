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
              withEnv(['GCLOUD_PATH=/home/google-cloud-sdk/bin'])
		          sh './scripts/push.sh'
            }
        }

        stage('Deploy') {
            steps {
		          sh 'echo deploying image...'
            }
        }
    }
}
