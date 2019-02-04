#!/usr/bin/env bash

echo "Type the base api url, followed by [ENTER]: (defaults to https://t8wwrnycz5.execute-api.us-east-1.amazonaws.com/dev/ ) "

read incomingbase

base=${incomingbase:-"https://t8wwrnycz5.execute-api.us-east-1.amazonaws.com/dev/"}

echo "========== Query ==================="

curl -G "${base}query"

echo -e "\n====================================== Registration endpoint ================================="

curl -d '{ "mock-endpoint":true }' -H "Content-Type: application/json" -X POST "${base}register"

echo -e "\n====================================== Try to initiate a payment ================================="

curl -d '{ "method-1": 56223, "method-2": 76343 }' -H "Content-Type: application/json" -X POST "${base}initiate-payment-intent"

echo -e "\n===================================== End ========================================"

echo -e "\nApi endpoint is ok if the above x-amz-errortype is ok"