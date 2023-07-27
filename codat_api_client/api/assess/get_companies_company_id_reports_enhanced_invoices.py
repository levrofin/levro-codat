from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_integrity_contracts_reports_invoices_report import (
    CodatDataIntegrityContractsReportsInvoicesReport,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    *,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["page"] = page

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/companies/{companyId}/reports/enhancedInvoices".format(
            companyId=company_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatDataIntegrityContractsReportsInvoicesReport]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataIntegrityContractsReportsInvoicesReport.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatDataIntegrityContractsReportsInvoicesReport]:
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
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
) -> Response[CodatDataIntegrityContractsReportsInvoicesReport]:
    """
    Args:
        company_id (str):
        page (int):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataIntegrityContractsReportsInvoicesReport]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    *,
    client: AuthenticatedClient,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
) -> Optional[CodatDataIntegrityContractsReportsInvoicesReport]:
    """
    Args:
        company_id (str):
        page (int):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataIntegrityContractsReportsInvoicesReport
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
) -> Response[CodatDataIntegrityContractsReportsInvoicesReport]:
    """
    Args:
        company_id (str):
        page (int):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataIntegrityContractsReportsInvoicesReport]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: AuthenticatedClient,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
) -> Optional[CodatDataIntegrityContractsReportsInvoicesReport]:
    """
    Args:
        company_id (str):
        page (int):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataIntegrityContractsReportsInvoicesReport
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            page=page,
            page_size=page_size,
        )
    ).parsed
