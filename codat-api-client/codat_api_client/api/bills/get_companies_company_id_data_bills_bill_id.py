from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_contracts_datasets_bill import CodatDataContractsDatasetsBill
from ...types import Response


def _get_kwargs(
    company_id: str,
    bill_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/companies/{companyId}/data/bills/{billId}".format(client.base_url, companyId=company_id, billId=bill_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[CodatDataContractsDatasetsBill]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataContractsDatasetsBill.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[CodatDataContractsDatasetsBill]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    bill_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsDatasetsBill]:
    """
    Args:
        company_id (str):
        bill_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsBill]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        bill_id=bill_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    bill_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsDatasetsBill]:
    """
    Args:
        company_id (str):
        bill_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsBill]
    """

    return sync_detailed(
        company_id=company_id,
        bill_id=bill_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    bill_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsDatasetsBill]:
    """
    Args:
        company_id (str):
        bill_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsBill]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        bill_id=bill_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    bill_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsDatasetsBill]:
    """
    Args:
        company_id (str):
        bill_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsBill]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            bill_id=bill_id,
            client=client,
        )
    ).parsed
