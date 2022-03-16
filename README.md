# Python API

## Container

```
{
  docker build . -t python-api
  docker run --rm --name python-api -p 3000:80 -it python-api
}

{
  docker exec -it python-api bash
  uvicorn main:app --reload --port 3000
  docker stop python-api
}
```

## FastAPI

Home

```
xdg-open http://127.0.0.1:3000
```

OpenAPI

```
xdg-open http://127.0.0.1:3000/docs
```
