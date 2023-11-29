pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/AbhishekRaoV/Augmented_AI.git'
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
            }
        }

        stage('Generate Report') {
            steps {
                sh 'python3 -m coverage report'
            }
        }

        stage("Code Coverage"){
            steps{
                script{
                    sh "cat /var/lib/jenkins/workspace/${JOB_NAME}/binarytree.py"
                    sh "cat /var/lib/jenkins/workspace/${JOB_NAME}/binarytree.py | sgpt --code \"generate unit test cases\" --no-cache > CodeCoverage.txt  "
                    }
                }
            post{
                success {
                    archiveArtifacts artifacts: '**/CodeCoverage.txt'
                }
            }
        }
        stage("Code/Design Consistency"){
            steps{
                script{
                    sh "cat /var/lib/jenkins/workspace/${JOB_NAME}/binarytree.py | sgpt --code \"optimise the code for time complexity\" > CodeDesign_Consistency.txt"
                    }
                    }
            post{
                success {
                    archiveArtifacts artifacts: '**/CodeDesign_Consistency.txt'
                }
            }
        }

        stage("Documentation Generation"){
            steps{
                script{
                    sh "cat /var/lib/jenkins/workspace/${JOB_NAME}/binarytree.py | sgpt \"generate line by line documentation for this code\" --no-cache > Document.txt"
                        }
                    }
            post{
                success {
                    archiveArtifacts artifacts: 'Document.txt'
                }
            }
        }
    }
}
