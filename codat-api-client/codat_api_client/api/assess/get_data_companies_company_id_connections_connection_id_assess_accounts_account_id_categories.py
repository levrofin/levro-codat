from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_assess_data_contracts_account_categories_account_categories_model import (
    CodatAssessDataContractsAccountCategoriesAccountCategoriesModel,
)
from ...types import Response


def _get_kwargs(
    company_id: str,
    connection_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/data/companies/{companyId}/connections/{connectionId}/assess/accounts/{accountId}/categories".format(
        client.base_url, companyId=company_id, connectionId=connection_id, accountId=account_id
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
) -> Optional[CodatAssessDataContractsAccountCategoriesAccountCategoriesModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatAssessDataContractsAccountCategoriesAccountCategoriesModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[CodatAssessDataContractsAccountCategoriesAccountCategoriesModel]:
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
) -> Response[CodatAssessDataContractsAccountCategoriesAccountCategoriesModel]:
    """Gets the suggested and/or confirmed category for a specific account.

    Args:
        company_id (str):
        connection_id (str):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatAssessDataContractsAccountCategoriesAccountCategoriesModel]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        account_id=account_id,
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
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatAssessDataContractsAccountCategoriesAccountCategoriesModel]:
    """Gets the suggested and/or confirmed category for a specific account.

    Args:
        company_id (str):
        connection_id (str):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatAssessDataContractsAccountCategoriesAccountCategoriesModel]
    """

    return sync_detailed(
        company_id=company_id,
        connection_id=connection_id,
        account_id=account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    connection_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatAssessDataContractsAccountCategoriesAccountCategoriesModel]:
    """Gets the suggested and/or confirmed category for a specific account.

    Args:
        company_id (str):
        connection_id (str):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatAssessDataContractsAccountCategoriesAccountCategoriesModel]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        account_id=account_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    connection_id: str,
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatAssessDataContractsAccountCategoriesAccountCategoriesModel]:
    """Gets the suggested and/or confirmed category for a specific account.

    Args:
        company_id (str):
        connection_id (str):
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatAssessDataContractsAccountCategoriesAccountCategoriesModel]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            connection_id=connection_id,
            account_id=account_id,
            client=client,
        )
    ).parsed
