from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    company_id: str,
    connection_id: str,
    bank_account_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "delete",
        "url": "/companies/{companyId}/connections/{connectionId}/connectionInfo/bankFeedAccounts/{bankAccountId}".format(
            companyId=company_id,
            connectionId=connection_id,
            bankAccountId=bank_account_id,
        ),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    connection_id: str,
    bank_account_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Delete a single BankFeed BankAccount for a single data source connected to a single company.

    Args:
        company_id (str):
        connection_id (str):
        bank_account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        bank_account_id=bank_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    company_id: str,
    connection_id: str,
    bank_account_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Delete a single BankFeed BankAccount for a single data source connected to a single company.

    Args:
        company_id (str):
        connection_id (str):
        bank_account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        bank_account_id=bank_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)