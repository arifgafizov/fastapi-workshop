from fastapi import FastAPI

from .api.routers import router

tags_metadata = [
    {
        'name': 'auth',
        'description': 'Авторизация и регистрация',
    },
    {
        'name': 'operations',
        'description': 'Работа с операциями',
    },
    {
        'name': 'reports',
        'description': 'Импорт и Экспорт отчетов',
    }
]


app = FastAPI(
    title='Workshop API',
    description='Сервис учета личных доходов и расходов',
    version='1.0.0',
    openapi_tags=tags_metadata,
)
app.include_router(router)
