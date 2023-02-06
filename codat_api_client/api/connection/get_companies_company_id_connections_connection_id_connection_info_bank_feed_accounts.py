from http import HTTPStatus
from typing import Any, Dict, List, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_standardization_bank_feeds_accounts_contract_bank_feed_bank_account import (
    CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount,
)
from ...types import Response


def _get_kwargs(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/companies/{companyId}/connections/{connectionId}/connectionInfo/bankFeedAccounts".format(
        client.base_url, companyId=company_id, connectionId=connection_id
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


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[List["CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[List["CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount"]]:
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
) -> Response[List["CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount"]]:
    """Get BankFeed BankAccounts for a single data source connected to a single company.

    Args:
        company_id (str):
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount']]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[List["CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount"]]:
    """Get BankFeed BankAccounts for a single data source connected to a single company.

    Args:
        company_id (str):
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount']]
    """

    return sync_detailed(
        company_id=company_id,
        connection_id=connection_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[List["CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount"]]:
    """Get BankFeed BankAccounts for a single data source connected to a single company.

    Args:
        company_id (str):
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount']]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[List["CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount"]]:
    """Get BankFeed BankAccounts for a single data source connected to a single company.

    Args:
        company_id (str):
        connection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount']]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            connection_id=connection_id,
            client=client,
        )
    ).parsed
