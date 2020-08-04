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
		          sh 'echo deploying image...'
            }
        }
    }
}
