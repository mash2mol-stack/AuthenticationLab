
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Получение исходного кода проекта'
            }
        }

        stage('Setup') {
            steps {
                echo 'Подготовка окружения'
            }
        }

        stage('Lint') {
            steps {
                echo 'Проверка качества кода'
            }
        }

        stage('Test') {
            steps {
                echo 'Запуск автоматических тестов'
            }
        }

        stage('Archive') {
            steps {
                echo 'Завершение конвейера'
            }
        }
    }
}
