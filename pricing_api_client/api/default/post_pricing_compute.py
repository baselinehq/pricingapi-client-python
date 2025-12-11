from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.github_com_baselinehq_golang_shared_types_instance import GithubComBaselinehqGolangSharedTypesInstance
from ...models.schema_compute_pricings_row import SchemaComputePricingsRow
from ...types import Response


def _get_kwargs(
    *,
    body: GithubComBaselinehqGolangSharedTypesInstance,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/pricing/compute",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SchemaComputePricingsRow | None:
    if response.status_code == 200:
        response_200 = SchemaComputePricingsRow.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SchemaComputePricingsRow]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GithubComBaselinehqGolangSharedTypesInstance,
) -> Response[SchemaComputePricingsRow]:
    """Get  pricing for an instance

     Get pricing

    Args:
        body (GithubComBaselinehqGolangSharedTypesInstance):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SchemaComputePricingsRow]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: GithubComBaselinehqGolangSharedTypesInstance,
) -> SchemaComputePricingsRow | None:
    """Get  pricing for an instance

     Get pricing

    Args:
        body (GithubComBaselinehqGolangSharedTypesInstance):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SchemaComputePricingsRow
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GithubComBaselinehqGolangSharedTypesInstance,
) -> Response[SchemaComputePricingsRow]:
    """Get  pricing for an instance

     Get pricing

    Args:
        body (GithubComBaselinehqGolangSharedTypesInstance):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SchemaComputePricingsRow]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: GithubComBaselinehqGolangSharedTypesInstance,
) -> SchemaComputePricingsRow | None:
    """Get  pricing for an instance

     Get pricing

    Args:
        body (GithubComBaselinehqGolangSharedTypesInstance):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SchemaComputePricingsRow
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
