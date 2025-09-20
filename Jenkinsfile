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
                 ssh -i $SSH_KEY -o StrictHostKeyChecking=no vagrant@lb.local whoami
                }
            }
        }
    }
}
