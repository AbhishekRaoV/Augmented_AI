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
                sh 'bandit -r binarytree.py'
            }
        }

        stage('Test Script') {
            steps {
                sh 'python3 -m coverage run binarytree.py'
                sh 'python3 -m coverage report'
            }
        }
 stage('Code Analysis '){
            steps{
                script{
                     sh '''
                        
                        pylint binarytree.py > ReviewFile.txt | cat binarytree.py | sgpt " rectify the code based on ReviewFile.txt and make changes" > temp.py --no-cache 
                        sed -n '/```python/,/```/ {/```python/!{/```/!p;}}' temp.py > binarytree.py
                        cat binarytree.py
                        cat ReviewFile.txt
                        git add binarytree.py
                        git config --global user.email "abhishekraovelichala@gmail.com"
                        git config --global user.name "AbhishekRaoV"
                        git commit -a -m 'Changes pushed by jenkins to test' || true
                        git push https://AbhishekRaoV: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@github.com/AbhishekRaoV/Augmented_AI.git main
                
                        
                        '''
                    
                }
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
