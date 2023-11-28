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
                sh 'python3 binarytree.py'
            }
        }

        stage('Scan with Bandit') {
            steps {
                sh 'bandit -r binarytree.py'
            }
        }
    }
}
