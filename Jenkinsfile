pipeline {
  agent { label 'Node1' }

  stages {
    stage('Checkout') {
      steps {
        // Récupère les playbooks Ansible depuis le repo Git
        git branch: 'main', url: 'https://github.com/quinquinc/noteapp.git'
      }
    }
    stage('Install Docker') {
      steps {
        // Exécute les commandes Ansible pour déployer les playbooks sur lagent Node 1
        sh 'ansible-playbook -i /home/admin/workspace/Test/Ansible/inventory /home/admin/workspace/Test/Ansible/InstallDockerGit.yml'
      }
    }

    stage('Deploy') {
      steps {
        // Exécute les commandes Ansible pour déployer les playbooks sur lagent Node 1
        sh 'ansible-playbook -i /home/admin/workspace/Test/Ansible/inventory /home/admin/workspace/Test/Ansible/DeployDockerImage.yml'
      }
    }

  }
}

