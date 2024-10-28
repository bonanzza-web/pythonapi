pipeline {
  agent any
  environment {
        KUBERNETES_SERVER = 'http://192.168.0.88:16443'
        K8S_TOKEN = credentials('microk8s')
    }
         stages {
           stage ('Hello') {
             steps {
               echo 'Hello world'
             }
           }
           stage ('Kubectl check') {
             steps {
               sh 'kubectl version --client'
             }
           }
           stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh '''
                    kubectl config set-credentials jenkins --token=$K8S_TOKEN
                    kubectl config set-cluster k8s-cluster --server=$KUBERNETES_SERVER --insecure-skip-tls-verify=true
                    kubectl config set-context jenkins-context --cluster=k8s-cluster --user=jenkins
                    kubectl config use-context jenkins-context

                    # Пример команды для развертывания
                    kubectl get secret
                    '''
                }
            }
        }
         }
        
}
