pipeline {
    agent any

    stages {
        
        stage('common tasks') {
            steps {
                withCredentials([sshUserPrivateKey(
                    credentialsId: 'vagrantssh',
                    keyFileVariable: 'SSH_KEY',
                    usernameVariable: 'SSH_USER'
                )]) {
                    sh 'ansible --version'
                    sh 'ssh -i $SSH_KEY -o StrictHostKeyChecking=no vagrant@lb.local whoami'
                    sh 'ssh -i $SSH_KEY -o StrictHostKeyChecking=no vagrant@web.local whoami'
                    sh 'ssh -i $SSH_KEY -o StrictHostKeyChecking=no vagrant@db.local whoami'
                }
            }
        }

        stage('Configure vms in parallel') {
            parallel {
                stage('Configure lb') {
                    steps {
                        withCredentials([sshUserPrivateKey(
                            credentialsId: 'vagrantssh',
                            keyFileVariable: 'SSH_KEY',
                            usernameVariable: 'SSH_USER'
                        )]) {
                            sh 'cd ansible && ansible-playbook -i /vagrant/inventory lb_install_nginx.yml --private-key $SSH_KEY'
                      }
                  }
                }

                stage('Configure web') {
                     steps {
                        withCredentials([
                            string(credentialsId: 'dbuser', variable: 'DB_USER'),
                            string(credentialsId: 'dbpass', variable: 'DB_PASS'),
                            string(credentialsId: 'dbname', variable: 'DB_NAME'),
                            sshUserPrivateKey(
                                credentialsId: 'vagrantssh',
                                keyFileVariable: 'SSH_KEY',
                                usernameVariable: 'SSH_USER'
                            )
                        ]) {
                        sh '''
                            cd ansible && ansible-playbook -i /vagrant/inventory web_install_nginx.yml \
                            --private-key "$SSH_KEY" \
                            -e "db_user=${DB_USER}" \
                            -e "db_pass=${DB_PASS}" \
                            -e "db_name=${DB_NAME}"
                            '''
                      }
                  }
                }

                stage('Configure db') {
                    steps {
                        withCredentials([
                            string(credentialsId: 'dbuser', variable: 'DB_USER'),
                            string(credentialsId: 'dbpass', variable: 'DB_PASS'),
                            string(credentialsId: 'dbname', variable: 'DB_NAME'),
                            sshUserPrivateKey(
                                credentialsId: 'vagrantssh',
                                keyFileVariable: 'SSH_KEY',
                                usernameVariable: 'SSH_USER'
                            )
                        ]) {
                            sh '''
                            cd ansible && ansible-playbook -i /vagrant/inventory install_psql.yml \
                            --private-key "$SSH_KEY" \
                            -e "db_user=${DB_USER}" \
                            -e "db_pass=${DB_PASS}" \
                            -e "db_name=${DB_NAME}"
                            '''
                        }                   }
               }
           }
      }
}
}
