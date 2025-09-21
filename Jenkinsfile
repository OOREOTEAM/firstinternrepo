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
                sh "ssh -i $SSH_KEY -o StrictHostKeyChecking=no vagrant@lb.local whoami"
                sh "ssh -i $SSH_KEY -o StrictHostKeyChecking=no vagrant@web.local whoami"
                sh "ssh -i $SSH_KEY -o StrictHostKeyChecking=no vagrant@db.local whoami"
                     
                }
                 withCredentials([sshUserPrivateKey(
                    credentialsId: 'vagrantssh',
                    keyFileVariable: 'SSH_KEY',
                    usernameVariable: 'SSH_USER'
                )]) {
                sh 'ansible -i /vagrant/inventory lb -m ping --private-key $SSH_KEY'
                }

                  withCredentials([sshUserPrivateKey(
                    credentialsId: 'vagrantssh',
                    keyFileVariable: 'SSH_KEY',
                    usernameVariable: 'SSH_USER'
                )]) {
                sh 'cd ansible && ansible-playbook -i /vagrant/inventory lb_install_nginx.yml --private-key $SSH_KEY'
                sh 'cd ansible && ansible-playbook -i /vagrant/inventory web_install_nginx.yml --private-key $SSH_KEY'
                //sh 'cd ansible && ansible-playbook -i /vagrant/inventory install_psql.yml --private-key  $SSH_KEY'
                sh 'cd /vagrant && ls'
                  }   
                  withCredentials([
                    string(credentialsId: 'dbuser', variable: 'DB_USER'),
                    string(credentialsId: 'dbpass', variable: 'DB_PASS'),
                    string(credentialsId: 'dbname', variable: 'DB_NAME'),
                    sshUserPrivateKey(
                    credentialsId: 'vagrantssh',
                    keyFileVariable: 'SSH_KEY_FILE',
                    usernameVariable: 'SSH_USER'
                   )]
                   ) {
                sh '''
                cd ansible && ansible-playbook -i /vagrant/inventory install_psql.yml \
                --private-key  "$SSH_KEY" \
                -e "db_user=${DB_USER}" \
                -e "db_pass=${DB_PASS}" \
                -e "db_name=${DB_NAME}"
                '''
              
                  }       
                
            }
        }
    }
}
