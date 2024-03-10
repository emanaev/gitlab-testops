# gitlab-testops
Start test Gitlab in docker and connect to it

Create `.env` file with GITLAB token
```
TOKEN=some-token-string123
```

Start with `docker-compose` - it will wait until Gitlab is started and token is registered:
```
docker-compose up -d
```

