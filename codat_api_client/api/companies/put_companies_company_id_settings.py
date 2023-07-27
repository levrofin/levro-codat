from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_clients_api_client_contract_company_settings import CodatClientsApiClientContractCompanySettings
from ...models.codat_public_api_models_company_company_settings import CodatPublicApiModelsCompanyCompanySettings
from ...types import Response


def _get_kwargs(
    company_id: str,
    *,
    json_body: CodatClientsApiClientContractCompanySettings,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/companies/{companyId}/settings".format(
            companyId=company_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatPublicApiModelsCompanyCompanySettings]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatPublicApiModelsCompanyCompanySettings.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
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
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
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
        CodatPublicApiModelsCompanyCompanySettings
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
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

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
        CodatPublicApiModelsCompanyCompanySettings
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
