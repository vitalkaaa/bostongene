#!/bin/bash

source venv/bin/activate;
celery worker -A tasks.tasks --autoscale=10,2
