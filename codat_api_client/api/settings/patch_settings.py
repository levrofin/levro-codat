from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_public_api_models_clients_client_settings_model import (
    CodatPublicApiModelsClientsClientSettingsModel,
)
from ...models.codat_public_api_models_clients_client_settings_patch_model import (
    CodatPublicApiModelsClientsClientSettingsPatchModel,
)
from ...types import Response


def _get_kwargs(
    *,
    json_body: CodatPublicApiModelsClientsClientSettingsPatchModel,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": "/settings",
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatPublicApiModelsClientsClientSettingsModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatPublicApiModelsClientsClientSettingsModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatPublicApiModelsClientsClientSettingsModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsClientsClientSettingsPatchModel,
) -> Response[CodatPublicApiModelsClientsClientSettingsModel]:
    """Update your settings

    Args:
        json_body (CodatPublicApiModelsClientsClientSettingsPatchModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsClientsClientSettingsModel]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsClientsClientSettingsPatchModel,
) -> Optional[CodatPublicApiModelsClientsClientSettingsModel]:
    """Update your settings

    Args:
        json_body (CodatPublicApiModelsClientsClientSettingsPatchModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatPublicApiModelsClientsClientSettingsModel
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsClientsClientSettingsPatchModel,
) -> Response[CodatPublicApiModelsClientsClientSettingsModel]:
    """Update your settings

    Args:
        json_body (CodatPublicApiModelsClientsClientSettingsPatchModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsClientsClientSettingsModel]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsClientsClientSettingsPatchModel,
) -> Optional[CodatPublicApiModelsClientsClientSettingsModel]:
    """Update your settings

    Args:
        json_body (CodatPublicApiModelsClientsClientSettingsPatchModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatPublicApiModelsClientsClientSettingsModel
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
