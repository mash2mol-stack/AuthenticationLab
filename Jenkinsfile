
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Получение проекта из GitHub'
                checkout scm
                bat 'dir'
            }
        }

        stage('Setup') {
            steps {
                echo 'Создание виртуального окружения'
                bat 'python --version'
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                echo 'Проверка кода через Flake8'
                bat '.venv\\Scripts\\python.exe -m flake8 . --exclude=.venv,.git'
            }
        }

        stage('Test') {
            steps {
                echo 'Запуск автоматических тестов'
                bat 'if not exist reports mkdir reports'

                script {
                    def result = bat(
                        returnStatus: true,
                        script: '.venv\\Scripts\\python.exe -m pytest -v --junitxml=reports\\junit.xml'
                    )

                    junit testResults: 'reports/junit.xml'

                    if (result != 0) {
                        error('Автоматические тесты завершились с ошибками')
                    }
                }
            }
        }

        stage('Archive') {
            steps {
                echo 'Подготовка результатов сборки'
                bat 'echo Build %BUILD_NUMBER% > reports\\build-info.txt'
                archiveArtifacts artifacts: 'reports/**', fingerprint: true
            }
        }
    }

    post {
        always {
            echo "Конвейер завершён. Сборка: ${env.BUILD_NUMBER}"
        }

        success {
            echo 'Все этапы выполнены успешно!'
        }

        failure {
            echo 'При выполнении конвейера обнаружена ошибка.'
        }
    }
}
