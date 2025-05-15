pipeline {
    agent any
    stages {
        stage("Checkout") {
            steps {
                git url: 'https://github.com/pps10219513/python', branch: "main"
            }
        }
        stage('Unit Test') {
               steps {
                    sh '''
                    python3 -m unittest discover -v
                    '''
               }
        }
    }
}

