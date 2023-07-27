from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_public_api_models_clients_integration_settings_model import (
    CodatPublicApiModelsClientsIntegrationSettingsModel,
)
from ...models.codat_public_api_models_clients_integration_settings_patch_model import (
    CodatPublicApiModelsClientsIntegrationSettingsPatchModel,
)
from ...types import Response


def _get_kwargs(
    integration_id: str,
    *,
    json_body: CodatPublicApiModelsClientsIntegrationSettingsPatchModel,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": "/settings/integrations/{integrationId}".format(
            integrationId=integration_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatPublicApiModelsClientsIntegrationSettingsModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatPublicApiModelsClientsIntegrationSettingsModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatPublicApiModelsClientsIntegrationSettingsModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    integration_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsClientsIntegrationSettingsPatchModel,
) -> Response[CodatPublicApiModelsClientsIntegrationSettingsModel]:
    """Update your organisations integration settings

    Args:
        integration_id (str):
        json_body (CodatPublicApiModelsClientsIntegrationSettingsPatchModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsClientsIntegrationSettingsModel]
    """

    kwargs = _get_kwargs(
        integration_id=integration_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    integration_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsClientsIntegrationSettingsPatchModel,
) -> Optional[CodatPublicApiModelsClientsIntegrationSettingsModel]:
    """Update your organisations integration settings

    Args:
        integration_id (str):
        json_body (CodatPublicApiModelsClientsIntegrationSettingsPatchModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatPublicApiModelsClientsIntegrationSettingsModel
    """

    return sync_detailed(
        integration_id=integration_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    integration_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsClientsIntegrationSettingsPatchModel,
) -> Response[CodatPublicApiModelsClientsIntegrationSettingsModel]:
    """Update your organisations integration settings

    Args:
        integration_id (str):
        json_body (CodatPublicApiModelsClientsIntegrationSettingsPatchModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsClientsIntegrationSettingsModel]
    """

    kwargs = _get_kwargs(
        integration_id=integration_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    integration_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsClientsIntegrationSettingsPatchModel,
) -> Optional[CodatPublicApiModelsClientsIntegrationSettingsModel]:
    """Update your organisations integration settings

    Args:
        integration_id (str):
        json_body (CodatPublicApiModelsClientsIntegrationSettingsPatchModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatPublicApiModelsClientsIntegrationSettingsModel
    """

    return (
        await asyncio_detailed(
            integration_id=integration_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
