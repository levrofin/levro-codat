from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_public_api_models_clients_integration_branding_model import (
    CodatPublicApiModelsClientsIntegrationBrandingModel,
)
from ...types import Response


def _get_kwargs(
    platform_key: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/integrations/{platformKey}/branding".format(
            platformKey=platform_key,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatPublicApiModelsClientsIntegrationBrandingModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatPublicApiModelsClientsIntegrationBrandingModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatPublicApiModelsClientsIntegrationBrandingModel]:
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
) -> Response[CodatPublicApiModelsClientsIntegrationBrandingModel]:
    """
    Args:
        platform_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsClientsIntegrationBrandingModel]
    """

    kwargs = _get_kwargs(
        platform_key=platform_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    platform_key: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatPublicApiModelsClientsIntegrationBrandingModel]:
    """
    Args:
        platform_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatPublicApiModelsClientsIntegrationBrandingModel
    """

    return sync_detailed(
        platform_key=platform_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    platform_key: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatPublicApiModelsClientsIntegrationBrandingModel]:
    """
    Args:
        platform_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsClientsIntegrationBrandingModel]
    """

    kwargs = _get_kwargs(
        platform_key=platform_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    platform_key: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatPublicApiModelsClientsIntegrationBrandingModel]:
    """
    Args:
        platform_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatPublicApiModelsClientsIntegrationBrandingModel
    """

    return (
        await asyncio_detailed(
            platform_key=platform_key,
            client=client,
        )
    ).parsed
