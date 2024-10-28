pipeline {
  agent any
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
         }
        
}
