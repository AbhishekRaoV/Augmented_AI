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
                sh 'python3 binarytree.py'
            }
        }

        stage('Scan Python Script') {
            steps {
                sh 'mypy binarytree.py'
            }
        }
    }
}
