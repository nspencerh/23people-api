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
		sh 'echo pushing image...'
            }
        }

        stage('Deploy') {
            steps {
		sh 'echo deploying image...'
            }
        }
    }
}
