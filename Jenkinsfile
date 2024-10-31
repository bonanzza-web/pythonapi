pipeline {
  agent any
  environment {
        KUBERNETES_SERVER = 'https://192.168.0.88:16443'
        K8S_TOKEN = credentials('microk8s')
    }
         stages {
           stage('SonarQube analysis') {
            steps {
                withSonarQubeEnv('sonar') {
                    sh '/var/jenkins_home/tools/hudson.plugins.sonar.SonarRunnerInstallation/sonarscanner/bin/bin/sonar-scanner -Dsonar.projectKey=pythonapi -Dsonar.host.url=http://192.168.0.7:9000'
                }
            }
        }
          stage("Quality Gate") {
                  steps {
                      // Этот шаг ожидает завершения анализа и возвращает статус Quality Gate
                      timeout(time: 2, unit: 'MINUTES') { 
                          script {
                              def qg = waitForQualityGate()
                              if (qg.status != 'OK') {
                                  error "Pipeline aborted due to quality gate failure: ${qg.status}"
                              }
                          }
                      }
                  }
              }
           stage ('Kubectl check') {
             steps {
               sh 'kubectl version --client'
             }
           }
           stage ('Create ns with ansible') {
             steps {
               sh 'ansible-playbook -i ./ansible/inventory/hosts.txt ./ansible/playbook.yml' 
           }
        }
           stage ('Docker hub login') {
            steps {
              script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    }
                }
            }
           }
           stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh '''
                    kubectl config set-credentials jenkins --token=$K8S_TOKEN
                    kubectl config set-cluster microk8s-cluster --server=$KUBERNETES_SERVER --insecure-skip-tls-verify=true
                    kubectl config set-context jenkins-context --cluster=microk8s-cluster --user=jenkins
                    kubectl config use-context jenkins-context

                    # Пример команды для развертывания
                    kubectl get po -A
                    kubectl get svc -A
                    '''
                }
            }
        }
            stage('Test test') {
              steps {
                sh 'python3 test.py'
              }
            }
         }
        
}
