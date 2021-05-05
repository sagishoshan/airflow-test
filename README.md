# airflow-test
This repo was created to help you get started with [Airflow](https://airflow.apache.org/), in a very simple and quick way.

## requirements
- [Docker](https://www.docker.com/)
- [make](https://www.tutorialspoint.com/unix_commands/make.htm)

## get started
- in your cmd, type 'make serve' (this will trigger the command to spin a new container with your Airflow app and this project's DAGs.)
- check http://localhost:3000/ to see your app

## get moving
start building your own tasks and wrap them with your own DAGs!
remember, there are multiple possible Operators that you can use.
this project contains a single example, but you can find more here

### note
The app is running using Docker image of [@puckel](https://github.com/puckel) . more information about it is available [here](https://github.com/puckel/docker-airflow)

### note 2
You can find a lot of examples for additional DAGs in the official [Airflow](https://github.com/apache/airflow) open-source [here](https://github.com/apache/airflow/tree/master/airflow/example_dags)
