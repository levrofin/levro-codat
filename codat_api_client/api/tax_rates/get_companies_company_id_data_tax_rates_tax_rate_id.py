from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_contracts_datasets_tax_rate import CodatDataContractsDatasetsTaxRate
from ...types import Response


def _get_kwargs(
    company_id: str,
    tax_rate_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/companies/{companyId}/data/taxRates/{taxRateId}".format(
        client.base_url, companyId=company_id, taxRateId=tax_rate_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[CodatDataContractsDatasetsTaxRate]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataContractsDatasetsTaxRate.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[CodatDataContractsDatasetsTaxRate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    tax_rate_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsDatasetsTaxRate]:
    """Gets the specified tax rate for a given company.

    Args:
        company_id (str):
        tax_rate_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsTaxRate]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        tax_rate_id=tax_rate_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    tax_rate_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsDatasetsTaxRate]:
    """Gets the specified tax rate for a given company.

    Args:
        company_id (str):
        tax_rate_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsTaxRate]
    """

    return sync_detailed(
        company_id=company_id,
        tax_rate_id=tax_rate_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    tax_rate_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsDatasetsTaxRate]:
    """Gets the specified tax rate for a given company.

    Args:
        company_id (str):
        tax_rate_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsTaxRate]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        tax_rate_id=tax_rate_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    tax_rate_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsDatasetsTaxRate]:
    """Gets the specified tax rate for a given company.

    Args:
        company_id (str):
        tax_rate_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsTaxRate]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            tax_rate_id=tax_rate_id,
            client=client,
        )
    ).parsed