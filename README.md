## how to test:

- set environment variables:
    - echo "export MIDIGATOR_SANDBOX_USERNAME=‘***'" >> ~/.zshrc
    - echo "export MIDIGATOR_SANDBOX_PASSWORD='***'" >> ~/.zshrc
    - source ~/.zshrc
- run run.py
- use postman to test the following links(basic auth, use the username/pwd above, GET):
    - http://127.0.0.1:5000/api/v1/midigator/
    - http://127.0.0.1:5000/api/v1/midigator/order (required mongodb)
    - http://127.0.0.1:5000/api/v1/midigator/user (required mongodb)

## to do:

- deploy to public access
- log system
- rate control
- run as docker container