from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_standardization_bank_feeds_accounts_contract_bank_feed_bank_account import (
    CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount,
)
from ...models.system_io_stream import SystemIOStream
from ...types import Response


def _get_kwargs(
    company_id: str,
    connection_id: str,
    *,
    json_body: CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/companies/{companyId}/connections/{connectionId}/connectionInfo/bankFeedAccounts".format(
            companyId=company_id,
            connectionId=connection_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SystemIOStream]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SystemIOStream.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SystemIOStream]:
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
    json_body: CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount,
) -> Response[SystemIOStream]:
    """Post a BankFeed BankAccount for a single data source connected to a single company.

    Args:
        company_id (str):
        connection_id (str):
        json_body (CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SystemIOStream]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        json_body=json_body,
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
    json_body: CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount,
) -> Optional[SystemIOStream]:
    """Post a BankFeed BankAccount for a single data source connected to a single company.

    Args:
        company_id (str):
        connection_id (str):
        json_body (CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SystemIOStream
    """

    return sync_detailed(
        company_id=company_id,
        connection_id=connection_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount,
) -> Response[SystemIOStream]:
    """Post a BankFeed BankAccount for a single data source connected to a single company.

    Args:
        company_id (str):
        connection_id (str):
        json_body (CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SystemIOStream]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount,
) -> Optional[SystemIOStream]:
    """Post a BankFeed BankAccount for a single data source connected to a single company.

    Args:
        company_id (str):
        connection_id (str):
        json_body (CodatStandardizationBankFeedsAccountsContractBankFeedBankAccount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SystemIOStream
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            connection_id=connection_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
