.PHONY: serve
serve: ## Start the AirFlow webserver
	docker run --name sagi-airflow -d -p 3000:8080 -v $(PWD)/airflow/dags:/usr/local/airflow/dags -v $(PWD)/requirements.txt:/requirements.txt puckel/docker-airflow webserver
