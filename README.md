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

Open a new terminal tab to run the asynchronous task to populate ElasticSearch:

```
vagrant ssh
workon github_top_contributors
cd /vagrant/data_collector/
ipython
In [1]: from app import celery
In [2]: celery.send_task("run_github_users_aggregator")
```

If you want to see the output while the process is running, you can open the following log file:

```
tail -f /var/log/supervisor/celery_supervisor.log
```

## Test API
Now you can open your web-browser at:

```
http://172.16.1.10/api/v1_0/search/?location=barcelona&page_size=50
```