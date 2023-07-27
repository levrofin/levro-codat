from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_assess_data_contracts_loans_loan_transactions_report import (
    CodatAssessDataContractsLoansLoanTransactionsReport,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    *,
    source_type: str,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["sourceType"] = source_type

    params["page"] = page

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/companies/{companyId}/reports/enhancedLiabilities/loan/transactions".format(
            companyId=company_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatAssessDataContractsLoansLoanTransactionsReport]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatAssessDataContractsLoansLoanTransactionsReport.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatAssessDataContractsLoansLoanTransactionsReport]:
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
    source_type: str,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
) -> Response[CodatAssessDataContractsLoansLoanTransactionsReport]:
    """
    Args:
        company_id (str):
        source_type (str):
        page (int):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatAssessDataContractsLoansLoanTransactionsReport]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        source_type=source_type,
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
    source_type: str,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
) -> Optional[CodatAssessDataContractsLoansLoanTransactionsReport]:
    """
    Args:
        company_id (str):
        source_type (str):
        page (int):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatAssessDataContractsLoansLoanTransactionsReport
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        source_type=source_type,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    source_type: str,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
) -> Response[CodatAssessDataContractsLoansLoanTransactionsReport]:
    """
    Args:
        company_id (str):
        source_type (str):
        page (int):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatAssessDataContractsLoansLoanTransactionsReport]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        source_type=source_type,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: AuthenticatedClient,
    source_type: str,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
) -> Optional[CodatAssessDataContractsLoansLoanTransactionsReport]:
    """
    Args:
        company_id (str):
        source_type (str):
        page (int):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatAssessDataContractsLoansLoanTransactionsReport
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            source_type=source_type,
            page=page,
            page_size=page_size,
        )
    ).parsed
