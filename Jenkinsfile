pipeline {
    agent any
    
    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/AbhishekRaoV/Augmented_AI.git'
            }
        }
        
        stage('Run python script') {
            steps {
                sh 'python script.py'
            }
        }
        
        stage('Scan python script using mypy') {
            steps {
                sh 'mypy script.py'
            }
        }
    }
}
