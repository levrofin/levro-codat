from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_public_api_models_clients_banking_settings_models_bank_settings_dataset import (
    CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset,
)
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset,
) -> Dict[str, Any]:
    url = "{}/integrations/bankSettings".format(client.base_url)

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
) -> Optional[CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset,
) -> Response[CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset]:
    """
    Args:
        json_body (CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset,
) -> Optional[CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset]:
    """
    Args:
        json_body (CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset,
) -> Response[CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset]:
    """
    Args:
        json_body (CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset,
) -> Optional[CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset]:
    """
    Args:
        json_body (CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsClientsBankingSettingsModelsBankSettingsDataset]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
