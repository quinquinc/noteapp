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
    stage('Install Docker Git etc') {      
      agent { node { label 'ansible'} }
      environment {
        // Définit les variables d'environnement pour l'utilisateur distant et les informations d'authentification SSH
        remoteUser = 'admin'
        sshKey = credentials('f15d728b-2556-4716-b2c0-c56bd671fbc5')
      }
      steps {
        // Exécute les commandes Ansible pour déployer les playbooks sur l'agent distant
        withEnv(["ANSIBLE_CONFIG=Ansible/ansible.cfg"]) {
          sh "ansible-playbook -i Ansible/inventory Ansible/InstallDockerGit.yml"
        }
      }
    }
    
    stage('Deploiement image') {
      agent { node { label 'ansible'} }
      environment {
        // Définit les variables d'environnement pour l'utilisateur distant et les informations d'authentification SSH
        remoteUser = 'admin'
        sshKey = credentials('f15d728b-2556-4716-b2c0-c56bd671fbc5')
      }      
      steps {
        // Exécute les commandes Ansible pour déployer les playbooks sur l'agent distant
        withEnv(["ANSIBLE_CONFIG=Ansible/ansible.cfg"]) {
          sh "ansible-playbook -i Ansible/inventory Ansible/DeployDockerImage.yml"
        }
      }
    }
  }
}