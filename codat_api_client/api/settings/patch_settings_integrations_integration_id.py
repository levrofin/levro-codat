from http import HTTPStatus
from typing import Any, Dict, Optional

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
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsClientsIntegrationSettingsPatchModel,
) -> Dict[str, Any]:
    url = "{}/settings/integrations/{integrationId}".format(client.base_url, integrationId=integration_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[CodatPublicApiModelsClientsIntegrationSettingsModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatPublicApiModelsClientsIntegrationSettingsModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
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
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
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
        Response[CodatPublicApiModelsClientsIntegrationSettingsModel]
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
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

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
        Response[CodatPublicApiModelsClientsIntegrationSettingsModel]
    """

    return (
        await asyncio_detailed(
            integration_id=integration_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
