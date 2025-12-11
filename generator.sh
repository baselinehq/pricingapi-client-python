pip install pipx
pipx ensurepath
pipx install openapi-python-client --include-deps



HOSTED_PATH=`pwd`/openapi_doc.json
curl https://converter.swagger.io/api/convert?url=https://pricing.baselinehq.cloud/swagger/doc.json -o ${HOSTED_PATH}

rm -r pricing_api_client || true
pipx run openapi-python-client generate --path ${HOSTED_PATH} --meta uv
mv pricing-api-client/* .
rm -r pricing-api-client