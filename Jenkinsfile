
pipeline {
    agent any

    environment {
        PROJECT_NAME = 'AuthenticationLab'
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Получение проекта ${env.PROJECT_NAME}..."
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                echo 'Установка зависимостей...'
                bat 'python --version'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                echo 'Проверка качества кода...'
                bat 'python -m flake8 .'
            }
        }

        stage('Test') {
            steps {
                echo 'Запуск автоматических тестов...'
                bat 'python -m pytest -v'
            }
        }

        stage('Archive') {
            steps {
                echo 'Создание артефакта сборки...'
                bat 'if not exist artifacts mkdir artifacts'
                bat 'echo Build %BUILD_NUMBER% > artifacts\\build.txt'
                archiveArtifacts artifacts: 'artifacts/**'
            }
        }
    }

    post {
        always {
            echo "Pipeline завершён. Номер сборки: ${env.BUILD_NUMBER}"
        }
        success {
            echo 'Все этапы выполнены успешно!'
        }
        failure {
            echo 'При выполнении Pipeline возникла ошибка.'
        }
    }
}
