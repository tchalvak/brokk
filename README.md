# Harr
A billing system approach.


## The Overall Approach
When there are multiple consuming applications and systems, it is beneficial to avoid a monolithic code system because the various consumers are going to have different needs and need different functionality.  For example, some consuming systems may only accept credit cards, not alternate providers.  A monolithic application like laravel may bake in options that decrease much-needed flexibility.

Recommended process:

-  Mock endpoints for a few pieces of the business logic
- Create a quick pipeline from code to tests to deployment, CICD
- Create a prototype to iterate on & create functional tests 
- Replace prototype code with refactored code based on feedback/deeper understanding of the business needs and create an SDK reference implementation
- replace parts of production ecosystem with the new system

The first focus here will be the prototyping/CI stage.

### Principles
- Keep microservices small to allow comprehension and refactoring as needed.
- Don't let the internal implementation bleed out for external consumption, the API should act as a black box.
- Mock first, prototype second, finalize third.

### Parts
- **APIGateway & Serverless & Lambda**: For fast prototyping, using Infrastructure-as-code for cloudformation allows spinning up an api with lambdas fast.  I will use the "serverless framework" and the serverless.yml config file in this repository for creating the api.
- **Double entry bookkeeping** with debits and credits.
- **Codeship CI** for auto-testing.
- **Authentication**: In the future in order to avoid re-inventing the authentication wheel and get a stronger security footing, it might be worth using AWS's Cognito to get high quality authentication and accounts.

## Install


    npm install -g serverless

## Test
Install pytest and test requirements:

    pip3 install --user -r requirements.txt
    sudo pip3 install -U pytest

Run the api tests:

    python3 -m pytest ./src/tests

## Deploy Infrastructure

### Configure
You will need to set up an AWS IAM user with the appropriate serverless provisioning [provisioning permissions](https://serverless.com/framework/docs/providers/aws/guide/credentials/).

### Execute Deploy
Deploy infrastructure to cloudformation from the serverless.yml file and assets

    sls deploy -v
