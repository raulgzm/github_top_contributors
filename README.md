# Github Top Contributors

## Requirements
- Python 3.4+
- Flask 0.12+
- Flask-RESTful 0.3.6+

## Environment Installation

```
git clone https://github.com/raulgonzm/github_top_contributors.git
cd github_top_contributors
vagrant up
vagrant ssh
workon github_top_contributors
```

## Populate ElasticSearch

Open a terminal tab to run the distributed task Queue Consumer:

```
vagrant ssh
workon github_top_contributors
cd /vagrant/data_collector/
celery -A data_collector.app.celery worker -c 4 --loglevel=DEBUG --workdir /vagrant
```

Open a new terminal tab to run the asynchronous task to populate ElasticSearch:

```
vagrant ssh
workon github_top_contributors
cd /vagrant/data_collector/
ipython
In [1]: from app import celery
In [2]: celery.send_task("run_github_users_aggregator")
```

## Run Backend API Server

Now you can go in project root (/vagrant/backend_api) and run server:

```
workon github_top_contributors
cd /vagrant/backend_api/
python server.py 
```

This should give you something like this:

```
 * Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 126-723-095 
```

## Test API
Now you can open your web-browser at:

```
http://172.16.1.10/api/v1_0/search/?location=barcelona&page_size=50
```