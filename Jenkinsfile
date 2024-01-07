pipeline {
    agent {
        node {
            label 'agent-python'
        }
    }

    triggers {
        pollSCM '* * * * *'
    }

    stages {
        stage('build') {
            steps {
                echo 'Building app.'
            }
        }
        
        stage('test') {
            steps {
                sh '''
                python3 -m unittest 
                '''
            }
        }
        
        stage('deploy') {
            steps {
                echo 'Deploying app.'
            }
        }
    }
}