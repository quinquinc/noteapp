pipeline {
  agent any
  
  stages {
    stage('Checkout') {
      steps {
        // Récupère les playbooks Ansible depuis le dépôt Git
        checkout([$class: 'GitSCM', 
          branches: [[name: '*/main']], 
          doGenerateSubmoduleConfigurations: false, 
          extensions: [], 
          submoduleCfg: [], 
          userRemoteConfigs: [[url: 'https://github.com/quinquinc/noteapp.git']]
        ])
      }
    }
    stage('Install Ansible') {
      agent { node { label 'Node1' } }
      steps {
        // Installe Ansible sur l'agent Jenkins appelé Node1
        ansibleInstallation('ansible')
      }
    }
    stage('Deploy') {
      agent { node { label 'Node1' } }
      environment {
        // Définit les variables d'environnement pour l'utilisateur distant et les informations d'authentification SSH
        remoteUser = 'admin@ip-172-31-45-159'
        sshKey = credentials('id_rsa.pub')
      }
      steps {
        // Exécute les commandes Ansible pour déployer les playbooks sur l'agent distant
        sh "ansible-playbook -i Ansible/inventory --user='${remoteUser}' --private-key='${sshKey}' Ansible/InstallDockerGit.yml"
      }
    }
  }
}
