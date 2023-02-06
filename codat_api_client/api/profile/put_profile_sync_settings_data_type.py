from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_public_api_models_clients_client_sync_settings_single_put_model import (
    CodatPublicApiModelsClientsClientSyncSettingsSinglePutModel,
)
from ...models.codat_public_api_models_sync_settings_sync_setting_model import (
    CodatPublicApiModelsSyncSettingsSyncSettingModel,
)
from ...types import Response


def _get_kwargs(
    data_type: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsClientsClientSyncSettingsSinglePutModel,
) -> Dict[str, Any]:
    url = "{}/profile/syncSettings/{dataType}".format(client.base_url, dataType=data_type)

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
) -> Optional[CodatPublicApiModelsSyncSettingsSyncSettingModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatPublicApiModelsSyncSettingsSyncSettingModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[CodatPublicApiModelsSyncSettingsSyncSettingModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_type: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsClientsClientSyncSettingsSinglePutModel,
) -> Response[CodatPublicApiModelsSyncSettingsSyncSettingModel]:
    """
    Args:
        data_type (str):
        json_body (CodatPublicApiModelsClientsClientSyncSettingsSinglePutModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsSyncSettingsSyncSettingModel]
    """

    kwargs = _get_kwargs(
        data_type=data_type,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_type: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsClientsClientSyncSettingsSinglePutModel,
) -> Optional[CodatPublicApiModelsSyncSettingsSyncSettingModel]:
    """
    Args:
        data_type (str):
        json_body (CodatPublicApiModelsClientsClientSyncSettingsSinglePutModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsSyncSettingsSyncSettingModel]
    """

    return sync_detailed(
        data_type=data_type,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    data_type: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsClientsClientSyncSettingsSinglePutModel,
) -> Response[CodatPublicApiModelsSyncSettingsSyncSettingModel]:
    """
    Args:
        data_type (str):
        json_body (CodatPublicApiModelsClientsClientSyncSettingsSinglePutModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsSyncSettingsSyncSettingModel]
    """

    kwargs = _get_kwargs(
        data_type=data_type,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_type: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsClientsClientSyncSettingsSinglePutModel,
) -> Optional[CodatPublicApiModelsSyncSettingsSyncSettingModel]:
    """
    Args:
        data_type (str):
        json_body (CodatPublicApiModelsClientsClientSyncSettingsSinglePutModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsSyncSettingsSyncSettingModel]
    """

    return (
        await asyncio_detailed(
            data_type=data_type,
            client=client,
            json_body=json_body,
        )
    ).parsed
