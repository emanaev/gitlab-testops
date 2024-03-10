# gitlab-testops
Start test Gitlab in docker and connect to it

Create `.env` file with GITLAB token
```
TOKEN=some-token-string123
```

Start with `docker-compose` and wait until `ops` successfully connects to Gitlab:
```
docker-compose up -d
docker-compose logs -f ops
```


