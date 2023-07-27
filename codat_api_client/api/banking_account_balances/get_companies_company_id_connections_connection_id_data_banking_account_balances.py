from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_contracts_datasets_banking_account_balance_paged_response_model import (
    CodatDataContractsDatasetsBankingAccountBalancePagedResponseModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    connection_id: str,
    *,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
    query: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["page"] = page

    params["pageSize"] = page_size

    params["query"] = query

    params["orderBy"] = order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/companies/{companyId}/connections/{connectionId}/data/banking-accountBalances".format(
            companyId=company_id,
            connectionId=connection_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatDataContractsDatasetsBankingAccountBalancePagedResponseModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataContractsDatasetsBankingAccountBalancePagedResponseModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatDataContractsDatasetsBankingAccountBalancePagedResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
    query: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Response[CodatDataContractsDatasetsBankingAccountBalancePagedResponseModel]:
    """Gets a list of balances for a bank account including end-of-day batch balance or running balances
    per transaction.

    Args:
        company_id (str):
        connection_id (str):
        page (int):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 100.
        query (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsBankingAccountBalancePagedResponseModel]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        page=page,
        page_size=page_size,
        query=query,
        order_by=order_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
    query: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Optional[CodatDataContractsDatasetsBankingAccountBalancePagedResponseModel]:
    """Gets a list of balances for a bank account including end-of-day batch balance or running balances
    per transaction.

    Args:
        company_id (str):
        connection_id (str):
        page (int):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 100.
        query (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsBankingAccountBalancePagedResponseModel
    """

    return sync_detailed(
        company_id=company_id,
        connection_id=connection_id,
        client=client,
        page=page,
        page_size=page_size,
        query=query,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
    query: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Response[CodatDataContractsDatasetsBankingAccountBalancePagedResponseModel]:
    """Gets a list of balances for a bank account including end-of-day batch balance or running balances
    per transaction.

    Args:
        company_id (str):
        connection_id (str):
        page (int):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 100.
        query (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsBankingAccountBalancePagedResponseModel]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        page=page,
        page_size=page_size,
        query=query,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
    query: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Optional[CodatDataContractsDatasetsBankingAccountBalancePagedResponseModel]:
    """Gets a list of balances for a bank account including end-of-day batch balance or running balances
    per transaction.

    Args:
        company_id (str):
        connection_id (str):
        page (int):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 100.
        query (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsBankingAccountBalancePagedResponseModel
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            connection_id=connection_id,
            client=client,
            page=page,
            page_size=page_size,
            query=query,
            order_by=order_by,
        )
    ).parsed
