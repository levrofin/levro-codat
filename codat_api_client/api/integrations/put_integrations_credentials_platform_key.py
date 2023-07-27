from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.put_integrations_credentials_platform_key_json_body import PutIntegrationsCredentialsPlatformKeyJsonBody
from ...models.put_integrations_credentials_platform_key_response_200 import (
    PutIntegrationsCredentialsPlatformKeyResponse200,
)
from ...types import Response


def _get_kwargs(
    platform_key: str,
    *,
    json_body: PutIntegrationsCredentialsPlatformKeyJsonBody,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/integrations/credentials/{platformKey}".format(
            platformKey=platform_key,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PutIntegrationsCredentialsPlatformKeyResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PutIntegrationsCredentialsPlatformKeyResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PutIntegrationsCredentialsPlatformKeyResponse200]:
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
) -> Response[PutIntegrationsCredentialsPlatformKeyResponse200]:
    """Update credentials required to authenticate with an accounting platform

    Args:
        platform_key (str):
        json_body (PutIntegrationsCredentialsPlatformKeyJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutIntegrationsCredentialsPlatformKeyResponse200]
    """

    kwargs = _get_kwargs(
        platform_key=platform_key,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    platform_key: str,
    *,
    client: AuthenticatedClient,
    json_body: PutIntegrationsCredentialsPlatformKeyJsonBody,
) -> Optional[PutIntegrationsCredentialsPlatformKeyResponse200]:
    """Update credentials required to authenticate with an accounting platform

    Args:
        platform_key (str):
        json_body (PutIntegrationsCredentialsPlatformKeyJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutIntegrationsCredentialsPlatformKeyResponse200
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
) -> Response[PutIntegrationsCredentialsPlatformKeyResponse200]:
    """Update credentials required to authenticate with an accounting platform

    Args:
        platform_key (str):
        json_body (PutIntegrationsCredentialsPlatformKeyJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutIntegrationsCredentialsPlatformKeyResponse200]
    """

    kwargs = _get_kwargs(
        platform_key=platform_key,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    platform_key: str,
    *,
    client: AuthenticatedClient,
    json_body: PutIntegrationsCredentialsPlatformKeyJsonBody,
) -> Optional[PutIntegrationsCredentialsPlatformKeyResponse200]:
    """Update credentials required to authenticate with an accounting platform

    Args:
        platform_key (str):
        json_body (PutIntegrationsCredentialsPlatformKeyJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutIntegrationsCredentialsPlatformKeyResponse200
    """

    return (
        await asyncio_detailed(
            platform_key=platform_key,
            client=client,
            json_body=json_body,
        )
    ).parsed
