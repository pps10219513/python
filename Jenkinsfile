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
                    docker  build -t tester .
		    docker run tester:latest 
		    docker rmi tester
                    '''
               }
        }
    }
}

