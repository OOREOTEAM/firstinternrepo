pipeline {
    agent any

    stages {
        stage('Check Ansible Version') {
            steps {
                // Print which node is running
                sh 'echo "Running on $(hostname)"'

                // Check ansible version
                sh 'ansible --version'
                sh 'pwd'
                sh 'users'
                sh 'ip a'
                sshagent(credentials: ['vagrantssh']) {
                sh 'ansible -i inventory all -m ping'
            }
        }
    }
}
