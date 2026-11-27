
pipeline {
    agent any

<<<<<<< HEAD
    stages {
        stage('Checkout') {
            steps {
                echo 'Получение исходного кода проекта'
=======
    environment {
        PROJECT_NAME = 'AuthenticationLab'
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Получение проекта ${env.PROJECT_NAME}..."
                checkout scm
>>>>>>> e910159f6566847a93cb5b131e80d808000c2fb7
            }
        }

        stage('Setup') {
            steps {
<<<<<<< HEAD
                echo 'Подготовка окружения'
=======
                echo 'Установка зависимостей...'
                bat 'python --version'
                bat 'python -m pip install -r requirements.txt'
>>>>>>> e910159f6566847a93cb5b131e80d808000c2fb7
            }
        }

        stage('Lint') {
            steps {
<<<<<<< HEAD
                echo 'Проверка качества кода'
=======
                echo 'Проверка качества кода...'
                bat 'python -m flake8 .'
>>>>>>> e910159f6566847a93cb5b131e80d808000c2fb7
            }
        }

        stage('Test') {
            steps {
<<<<<<< HEAD
                echo 'Запуск автоматических тестов'
=======
                echo 'Запуск автоматических тестов...'
                bat 'python -m pytest -v'
>>>>>>> e910159f6566847a93cb5b131e80d808000c2fb7
            }
        }

        stage('Archive') {
            steps {
<<<<<<< HEAD
                echo 'Завершение конвейера'
            }
        }
    }
=======
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
>>>>>>> e910159f6566847a93cb5b131e80d808000c2fb7
}
