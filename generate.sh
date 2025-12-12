#!/usr/bin/env bash

set -e

pip install pipx
pipx ensurepath
pipx install openapi-generator-cli --include-deps

HOSTED_PATH=`pwd`/openapi_doc.json
curl https://pricing.baselinehq.cloud/swagger/doc.json -o ${HOSTED_PATH}

rm -r pricing_api_client || true
pipx run openapi-generator-cli generate -i ${HOSTED_PATH} -g python -o pricing-api-client --additional-properties=packageName=pricing_api_client
cp -r pricing-api-client/* .
rm -r pricing-api-client
rm openapi_doc.json

GIT_USER_ID=baselinehq
GIT_REPO_ID=pricingapi-client-python
export GIT_USER_ID
export GIT_REPO_ID
grep -RIlZ 'GIT_USER_ID' . --exclude-dir=.git --exclude=generate.sh | xargs -0 -r perl -i -pe 's/\bGIT_USER_ID\b/$ENV{GIT_USER_ID}/g'
grep -RIlZ 'GIT_REPO_ID' . --exclude-dir=.git --exclude=generate.sh | xargs -0 -r perl -i -pe 's/\bGIT_REPO_ID\b/$ENV{GIT_REPO_ID}/g'