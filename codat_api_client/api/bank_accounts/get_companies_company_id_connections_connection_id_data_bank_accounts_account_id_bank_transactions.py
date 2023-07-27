from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_contracts_datasets_bank_transaction_paged_response_model import (
    CodatDataContractsDatasetsBankTransactionPagedResponseModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    connection_id: str,
    account_id: str,
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
        "url": "/companies/{companyId}/connections/{connectionId}/data/bankAccounts/{accountId}/bankTransactions".format(
            companyId=company_id,
            connectionId=connection_id,
            accountId=account_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatDataContractsDatasetsBankTransactionPagedResponseModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataContractsDatasetsBankTransactionPagedResponseModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatDataContractsDatasetsBankTransactionPagedResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    connection_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
    query: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Response[CodatDataContractsDatasetsBankTransactionPagedResponseModel]:
    """Gets bank transactions for a given bank account ID

    Args:
        company_id (str):
        connection_id (str):
        account_id (str):
        page (int):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 100.
        query (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsBankTransactionPagedResponseModel]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        account_id=account_id,
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
    account_id: str,
    *,
    client: AuthenticatedClient,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
    query: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Optional[CodatDataContractsDatasetsBankTransactionPagedResponseModel]:
    """Gets bank transactions for a given bank account ID

    Args:
        company_id (str):
        connection_id (str):
        account_id (str):
        page (int):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 100.
        query (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsBankTransactionPagedResponseModel
    """

    return sync_detailed(
        company_id=company_id,
        connection_id=connection_id,
        account_id=account_id,
        client=client,
        page=page,
        page_size=page_size,
        query=query,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    connection_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
    query: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Response[CodatDataContractsDatasetsBankTransactionPagedResponseModel]:
    """Gets bank transactions for a given bank account ID

    Args:
        company_id (str):
        connection_id (str):
        account_id (str):
        page (int):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 100.
        query (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsBankTransactionPagedResponseModel]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        account_id=account_id,
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
    account_id: str,
    *,
    client: AuthenticatedClient,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
    query: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Optional[CodatDataContractsDatasetsBankTransactionPagedResponseModel]:
    """Gets bank transactions for a given bank account ID

    Args:
        company_id (str):
        connection_id (str):
        account_id (str):
        page (int):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 100.
        query (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsBankTransactionPagedResponseModel
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            connection_id=connection_id,
            account_id=account_id,
            client=client,
            page=page,
            page_size=page_size,
            query=query,
            order_by=order_by,
        )
    ).parsed
