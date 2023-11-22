pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/AbhishekRaoV/Augmented_AI.git'
            }
        }
        
        stage('Run Python Script') {
            steps {
                sh 'python binarytree.py'
            }
        }
        
        stage('Scan Python Script') {
            steps {
                sh 'mypy binarytree.py'
            }
        }
    }
}
