# Тестовое задание отдел бэкенд Сарафан

- Python 3.11
- Django 5
- DRF 3.14


### Запуск

```bash
    docker compose -f docker-compose-postgres.yaml up -d --build
```


#### Админка
http://127.0.0.1:8000/admin/
- логин: admin
- пароль: mysecretpassword

#### Токен
http://127.0.0.1:8000/api/token/login/
```json
{
"username": "admin",
"password": "mysecretpassword"
}
```

#### Категории
http://127.0.0.1:8000/api/categories/
```json
    {
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "name": "зелень",
            "slug": "zelen",
            "parent_id": 1,
            "image": null,
            "subcategories": []
        },
        {
            "id": 1,
            "name": "овощи",
            "slug": "ovoshi",
            "parent_id": null,
            "image": null,
            "subcategories": [
                {
                    "id": 2,
                    "name": "зелень",
                    "slug": "zelen",
                    "parent_id": 1,
                    "image": null,
                    "subcategories": []
                }
            ]
        }
    ]
}
```

#### Продукты
http://127.0.0.1:8000/api/products/
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "петрушка",
            "slug": "petrushka",
            "category": {
                "id": 2,
                "name": "зелень",
                "slug": "zelen",
                "parent_id": 1,
                "image": null,
                "subcategories": []
            },
            "price": "10.00",
            "images": []
        },
        {
            "name": "помидоры",
            "slug": "pomidory",
            "category": {
                "id": 1,
                "name": "овощи",
                "slug": "ovoshi",
                "parent_id": null,
                "image": null,
                "subcategories": [
                    {
                        "id": 2,
                        "name": "зелень",
                        "slug": "zelen",
                        "parent_id": 1,
                        "image": null,
                        "subcategories": []
                    }
                ]
            },
            "price": "20.00",
            "images": []
        }
    ]
}
```

#### Корзина
http://127.0.0.1:8000/api/shopping-cart/
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "cart_products": [
                {
                    "product": {
                        "id": 1,
                        "name": "петрушка",
                        "price": "10.00",
                        "slug": "petrushka",
                        "category": 2,
                        "images": []
                    },
                    "quantity": 5
                },
                {
                    "product": {
                        "id": 2,
                        "name": "помидоры",
                        "price": "20.00",
                        "slug": "pomidory",
                        "category": 1,
                        "images": []
                    },
                    "quantity": 10
                }
            ],
            "total_price": "250.00"
        }
    ]
}
```
