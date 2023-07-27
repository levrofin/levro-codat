from http import HTTPStatus
from typing import Any, Dict, Optional, Union

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
    json_body: CodatPublicApiModelsClientsClientSyncSettingsSinglePutModel,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/profile/syncSettings/{dataType}".format(
            dataType=data_type,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatPublicApiModelsSyncSettingsSyncSettingModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatPublicApiModelsSyncSettingsSyncSettingModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
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
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
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
        CodatPublicApiModelsSyncSettingsSyncSettingModel
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
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

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
        CodatPublicApiModelsSyncSettingsSyncSettingModel
    """

    return (
        await asyncio_detailed(
            data_type=data_type,
            client=client,
            json_body=json_body,
        )
    ).parsed
