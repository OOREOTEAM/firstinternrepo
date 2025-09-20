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
                 withCredentials([sshUserPrivateKey(
                    credentialsId: 'vagrantssh',
                    keyFileVariable: 'SSH_KEY',
                    usernameVariable: 'SSH_USER'
                )]) {
                 sh 'ssh -i ${keyfile} vagrant@lb.local
                }
            }
        }
    }
}
