#!/bin/sh
cd /usr/src/api/src && gunicorn main:api -b 0.0.0.0:8000 --reload