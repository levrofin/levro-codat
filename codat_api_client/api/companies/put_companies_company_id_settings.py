from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_clients_api_client_contract_company_settings import CodatClientsApiClientContractCompanySettings
from ...models.codat_public_api_models_company_company_settings import CodatPublicApiModelsCompanyCompanySettings
from ...types import Response


def _get_kwargs(
    company_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatClientsApiClientContractCompanySettings,
) -> Dict[str, Any]:
    url = "{}/companies/{companyId}/settings".format(client.base_url, companyId=company_id)

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
) -> Optional[CodatPublicApiModelsCompanyCompanySettings]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatPublicApiModelsCompanyCompanySettings.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[CodatPublicApiModelsCompanyCompanySettings]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatClientsApiClientContractCompanySettings,
) -> Response[CodatPublicApiModelsCompanyCompanySettings]:
    """Update settings on a single company.

    Args:
        company_id (str):
        json_body (CodatClientsApiClientContractCompanySettings):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsCompanyCompanySettings]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatClientsApiClientContractCompanySettings,
) -> Optional[CodatPublicApiModelsCompanyCompanySettings]:
    """Update settings on a single company.

    Args:
        company_id (str):
        json_body (CodatClientsApiClientContractCompanySettings):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsCompanyCompanySettings]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatClientsApiClientContractCompanySettings,
) -> Response[CodatPublicApiModelsCompanyCompanySettings]:
    """Update settings on a single company.

    Args:
        company_id (str):
        json_body (CodatClientsApiClientContractCompanySettings):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsCompanyCompanySettings]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatClientsApiClientContractCompanySettings,
) -> Optional[CodatPublicApiModelsCompanyCompanySettings]:
    """Update settings on a single company.

    Args:
        company_id (str):
        json_body (CodatClientsApiClientContractCompanySettings):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsCompanyCompanySettings]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
