pipeline {
    agent any

    stages {
        stage('Build Application') {
            steps {
                cd sample-app/;
                nodejs("11.9") { sh "npm install" }
            }
        }
        stage('Deploy Application') {
            steps {
	    	  cd sample-app/;
            	  nodejs("11.9") { sh "npm start &" }
            }
        }
        stage('Run Functional Tests') {
            steps {
                sauce('496fc4d5-5eac-43f3-813d-dc31708a20be') {
		    python3 -m venv venv;
		    source venv/bin/activate;
		    pip install -r requirements.txt
		    pytest tests/
                }
            }
        }
    }
}