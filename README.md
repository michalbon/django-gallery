# django-gallery

Running

```
docker-compose up web
```

## API

List of images in gallery
```
GET http://0.0.0.0:8001/gallery/
```

Post a new image
```
POST http://0.0.0.0:8001/gallery/
```

Update an image
```
PUT http://0.0.0.0:8001/gallery/<id>
```

Preview
```
GET http://0.0.0.0:8001/gallery/preview
```

## Tests and checks

Run `pytest`, `ruff` & `mypy`

```
docker-compose run tests-and-checks
```
