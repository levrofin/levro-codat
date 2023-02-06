from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_public_api_models_platform_credentials_enabled_args import (
    CodatPublicApiModelsPlatformCredentialsEnabledArgs,
)
from ...models.codat_public_api_models_platform_credentials_platform_source_model import (
    CodatPublicApiModelsPlatformCredentialsPlatformSourceModel,
)
from ...types import Response


def _get_kwargs(
    platform_key: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsPlatformCredentialsEnabledArgs,
) -> Dict[str, Any]:
    url = "{}/integrations/{platformKey}/enabled".format(client.base_url, platformKey=platform_key)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[CodatPublicApiModelsPlatformCredentialsPlatformSourceModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[CodatPublicApiModelsPlatformCredentialsPlatformSourceModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    platform_key: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsPlatformCredentialsEnabledArgs,
) -> Response[CodatPublicApiModelsPlatformCredentialsPlatformSourceModel]:
    """
    Args:
        platform_key (str):
        json_body (CodatPublicApiModelsPlatformCredentialsEnabledArgs):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsPlatformCredentialsPlatformSourceModel]
    """

    kwargs = _get_kwargs(
        platform_key=platform_key,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    platform_key: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsPlatformCredentialsEnabledArgs,
) -> Optional[CodatPublicApiModelsPlatformCredentialsPlatformSourceModel]:
    """
    Args:
        platform_key (str):
        json_body (CodatPublicApiModelsPlatformCredentialsEnabledArgs):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsPlatformCredentialsPlatformSourceModel]
    """

    return sync_detailed(
        platform_key=platform_key,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    platform_key: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsPlatformCredentialsEnabledArgs,
) -> Response[CodatPublicApiModelsPlatformCredentialsPlatformSourceModel]:
    """
    Args:
        platform_key (str):
        json_body (CodatPublicApiModelsPlatformCredentialsEnabledArgs):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsPlatformCredentialsPlatformSourceModel]
    """

    kwargs = _get_kwargs(
        platform_key=platform_key,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    platform_key: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsPlatformCredentialsEnabledArgs,
) -> Optional[CodatPublicApiModelsPlatformCredentialsPlatformSourceModel]:
    """
    Args:
        platform_key (str):
        json_body (CodatPublicApiModelsPlatformCredentialsEnabledArgs):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsPlatformCredentialsPlatformSourceModel]
    """

    return (
        await asyncio_detailed(
            platform_key=platform_key,
            client=client,
            json_body=json_body,
        )
    ).parsed
