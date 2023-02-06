from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_public_api_models_platform_credentials_platform_credentials import (
    CodatPublicApiModelsPlatformCredentialsPlatformCredentials,
)
from ...models.put_integrations_credentials_platform_key_json_body import PutIntegrationsCredentialsPlatformKeyJsonBody
from ...types import Response


def _get_kwargs(
    platform_key: str,
    *,
    client: AuthenticatedClient,
    json_body: PutIntegrationsCredentialsPlatformKeyJsonBody,
) -> Dict[str, Any]:
    url = "{}/integrations/credentials/{platformKey}".format(client.base_url, platformKey=platform_key)

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
) -> Optional[CodatPublicApiModelsPlatformCredentialsPlatformCredentials]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatPublicApiModelsPlatformCredentialsPlatformCredentials.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[CodatPublicApiModelsPlatformCredentialsPlatformCredentials]:
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
    json_body: PutIntegrationsCredentialsPlatformKeyJsonBody,
) -> Response[CodatPublicApiModelsPlatformCredentialsPlatformCredentials]:
    """Update credentials required to authenticate with an accounting platform

    Args:
        platform_key (str):
        json_body (PutIntegrationsCredentialsPlatformKeyJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsPlatformCredentialsPlatformCredentials]
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
    json_body: PutIntegrationsCredentialsPlatformKeyJsonBody,
) -> Optional[CodatPublicApiModelsPlatformCredentialsPlatformCredentials]:
    """Update credentials required to authenticate with an accounting platform

    Args:
        platform_key (str):
        json_body (PutIntegrationsCredentialsPlatformKeyJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsPlatformCredentialsPlatformCredentials]
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
    json_body: PutIntegrationsCredentialsPlatformKeyJsonBody,
) -> Response[CodatPublicApiModelsPlatformCredentialsPlatformCredentials]:
    """Update credentials required to authenticate with an accounting platform

    Args:
        platform_key (str):
        json_body (PutIntegrationsCredentialsPlatformKeyJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsPlatformCredentialsPlatformCredentials]
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
    json_body: PutIntegrationsCredentialsPlatformKeyJsonBody,
) -> Optional[CodatPublicApiModelsPlatformCredentialsPlatformCredentials]:
    """Update credentials required to authenticate with an accounting platform

    Args:
        platform_key (str):
        json_body (PutIntegrationsCredentialsPlatformKeyJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsPlatformCredentialsPlatformCredentials]
    """

    return (
        await asyncio_detailed(
            platform_key=platform_key,
            client=client,
            json_body=json_body,
        )
    ).parsed
