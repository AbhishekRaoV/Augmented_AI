pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/AbhishekRaoV/Augmented_AI.git'
            }
        }

        stage('Run Script') {
            steps {
                sh 'python3 binarytree.py'
            }
        }

        stage('Scan Script') {
            steps {
                sh 'bandit binarytree.py'
            }
        }

        stage('Test Script') {
            steps {
                sh 'python3 -m coverage run binarytree.py'
                sh 'python3 -m coverage report'
            }
        }
    }
}
pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/AbhishekRaoV/Augmented_AI.git'
            }
        }

        stage('Run Script') {
            steps {
                sh 'python3 binarytree.py'
            }
        }

        stage('Scan Script') {
            steps {
                sh 'bandit binarytree.py'
            }
        }

        stage('Test Script') {
            steps {
                sh 'python3 -m coverage run binarytree.py'
                sh 'python3 -m coverage report'
            }
        }
    }
}
