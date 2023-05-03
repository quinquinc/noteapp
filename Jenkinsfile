pipeline {
  agent any
  
  stages {
    stage('Checkout') {
      steps {
        // Récupère les playbooks Ansible depuis le dépôt Git
        checkout([$class: 'GitSCM', 
          branches: [[name: '*/master']], 
          doGenerateSubmoduleConfigurations: false, 
          extensions: [], 
          submoduleCfg: [], 
          userRemoteConfigs: [[url: 'https://github.com/quinquinc/noteapp.git']]
        ])
      }
    }
    //stage('Install Ansible') {
      //agent { node { label 'Node1' } }
      //steps {
        // Installe Ansible sur l'agent Jenkins appelé Node1
        //ansibleInstallation('ansible')
      //}
    //}
    stage('Deploy') {
      agent { node { label 'Node1' } }
      environment {
        // Définit les variables d'environnement pour l'utilisateur distant et les informations d'authentification SSH
        remoteUser = 'admin'
        sshKey = credentials('98d6794a-1824-46ca-b67b-c32692273529')
      }
      steps {
        // Exécute les commandes Ansible pour déployer les playbooks sur l'agent distant
        withEnv(["ANSIBLE_CONFIG=Ansible/ansible.cfg"]) {
          sh "ansible-playbook -i Ansible/inventory --user='${remoteUser}' --private-key='${sshKey}' Ansible/InstallDockerGit.yml"
        }
      }
    }
  }
}
