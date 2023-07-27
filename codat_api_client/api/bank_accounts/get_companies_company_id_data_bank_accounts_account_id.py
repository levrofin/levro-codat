from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_contracts_datasets_bank_statement_account import (
    CodatDataContractsDatasetsBankStatementAccount,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    account_id: str,
    *,
    query: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["query"] = query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/companies/{companyId}/data/bankAccounts/{accountId}".format(
            companyId=company_id,
            accountId=account_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatDataContractsDatasetsBankStatementAccount]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataContractsDatasetsBankStatementAccount.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatDataContractsDatasetsBankStatementAccount]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
    query: Union[Unset, None, str] = UNSET,
) -> Response[CodatDataContractsDatasetsBankStatementAccount]:
    """Gets the bank account for given account ID.

    Args:
        company_id (str):
        account_id (str):
        query (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsBankStatementAccount]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        account_id=account_id,
        query=query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
    query: Union[Unset, None, str] = UNSET,
) -> Optional[CodatDataContractsDatasetsBankStatementAccount]:
    """Gets the bank account for given account ID.

    Args:
        company_id (str):
        account_id (str):
        query (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsBankStatementAccount
    """

    return sync_detailed(
        company_id=company_id,
        account_id=account_id,
        client=client,
        query=query,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
    query: Union[Unset, None, str] = UNSET,
) -> Response[CodatDataContractsDatasetsBankStatementAccount]:
    """Gets the bank account for given account ID.

    Args:
        company_id (str):
        account_id (str):
        query (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsBankStatementAccount]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        account_id=account_id,
        query=query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
    query: Union[Unset, None, str] = UNSET,
) -> Optional[CodatDataContractsDatasetsBankStatementAccount]:
    """Gets the bank account for given account ID.

    Args:
        company_id (str):
        account_id (str):
        query (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsBankStatementAccount
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            account_id=account_id,
            client=client,
            query=query,
        )
    ).parsed
