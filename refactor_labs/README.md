# 📋 Restaurant Management System

![CI/CD Pipeline](https://github.com/zakulaza/devops_lab6/actions/workflows/ci.yml/badge.svg)
Сучасна система управління замовленнями ресторану, побудована на базі **FastAPI** та **MongoDB**. Проєкт реалізований з використанням принципів контейнеризації (Docker) та автоматизації процесів розробки (CI/CD).

---

## 🛠 Технологічний стек

* **Backend:** Python 3.10, FastAPI (Uvicorn)
* **Database:** MongoDB (NoSQL)
* **Containerization:** Docker, Docker Compose
* **CI/CD:** GitHub Actions
* **Testing:** Pytest
* **Linting:** Flake8

---

## 🚀 Швидкий запуск через Docker (Рекомендовано)

Цей метод автоматично підніме і додаток, і базу даних у зв'язці.

1.  **Клонуйте репозиторій:**
    ```bash
    git clone [https://github.com/zakulaza/devops_lab6.git](https://github.com/zakulaza/devops_lab6.git)
    cd devops_lab6
    ```
2.  **Запустіть систему:**
    ```bash
    docker-compose up --build
    ```
3.  **Перевірте результат:**
    Додаток буде доступний за адресою: [http://localhost:8000](http://localhost:8000)

---

## 💻 Локальний запуск (Development)

Для запуску без Docker вам знадобиться встановлена MongoDB локально.

1.  **Створіть та активуйте віртуальне середовище:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    ```
2.  **Встановіть залежності:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Запустіть сервер:**
    ```bash
    uvicorn src.main:app --reload
    ```

---

## ⚙️ Змінні середовища

У файлі `docker-compose.yaml` або локально можна налаштувати наступні параметри:

| Змінна | Опис | Значення за замовчуванням |
| :--- | :--- | :--- |
| `MONGO_URI` | Рядок підключення до бази даних | `mongodb://root:example@db:27017/` |
| `DB_NAME` | Назва NoSQL бази даних | `restaurant_db` |
| `ENVIRONMENT` | Режим роботи (dev/prod) | `production` |

---

## 📡 Основні API Ендпоінти

| Метод | Ендпоінт | Опис |
| :--- | :--- | :--- |
| `GET` | `/` | Стартова сторінка (Health check) |
| `GET` | `/orders` | Отримання списку всіх замовлень |
| `GET` | `/docs` | Автоматична документація Swagger UI |

---

## 🧪 Тестування та Контроль Якості

### Запуск тестів
Ми використовуємо **pytest** для автоматичного тестування бізнес-логіки:
```bash
python -m pytest tests/ -v
