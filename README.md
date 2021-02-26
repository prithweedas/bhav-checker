# Bhav Checker

The perpous of this project is to download Equity Bhavcopy everyday and provide an UI to easily search and download search result.

### Tech Stack
  - Django
  - Vue
  - Redis

## Steps to host this project
Requirements
  - crontab
  - python3.9
  - docker
  - docker compose


Steps
  - Clone this repo.
```shell
git clone git@github.com:prithweedas/bhav-checker.git
```
 - Go to the cloned repo. Build and start the docker containers using docker-compose. (-d is to start in detached mode)

```shell
docker-compose up -d
```
  - Run get_bhav_data.py to save initial data in redis.

  - set scripts/get_bhav_data.py as cronjob to execute everyday at 18:02

Open crontab using `crontab -e` and paste the following

```
2 18 * * * /path/to/python3.9 /path/to/cloned/repo/scripts/get_bhav_data.py
```
 - go to port 8000 to use it.


