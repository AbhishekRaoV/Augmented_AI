pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/AbhishekRaoV/Augmented_AI.git'
            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python binarytree.py'
            }
        }

        stage('Scan with Mypy') {
            steps {
                sh 'mypy binarytree.py'
            }
        }
    }
}
