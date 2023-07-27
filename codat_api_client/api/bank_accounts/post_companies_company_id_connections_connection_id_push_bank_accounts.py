from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_contracts_datasets_bank_account import CodatDataContractsDatasetsBankAccount
from ...models.codat_data_contracts_datasets_bank_account_push_operation import (
    CodatDataContractsDatasetsBankAccountPushOperation,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    connection_id: str,
    *,
    json_body: CodatDataContractsDatasetsBankAccount,
    allow_sync_on_push_complete: Union[Unset, None, bool] = True,
    timeout_in_minutes: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["allowSyncOnPushComplete"] = allow_sync_on_push_complete

    params["timeoutInMinutes"] = timeout_in_minutes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/companies/{companyId}/connections/{connectionId}/push/bankAccounts".format(
            companyId=company_id,
            connectionId=connection_id,
        ),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatDataContractsDatasetsBankAccountPushOperation]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataContractsDatasetsBankAccountPushOperation.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatDataContractsDatasetsBankAccountPushOperation]:
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
    json_body: CodatDataContractsDatasetsBankAccount,
    allow_sync_on_push_complete: Union[Unset, None, bool] = True,
    timeout_in_minutes: Union[Unset, None, int] = UNSET,
) -> Response[CodatDataContractsDatasetsBankAccountPushOperation]:
    """Posts a new bank account to the accounting package for a given company.

    Args:
        company_id (str):
        connection_id (str):
        allow_sync_on_push_complete (Union[Unset, None, bool]):  Default: True.
        timeout_in_minutes (Union[Unset, None, int]):
        json_body (CodatDataContractsDatasetsBankAccount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsBankAccountPushOperation]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        json_body=json_body,
        allow_sync_on_push_complete=allow_sync_on_push_complete,
        timeout_in_minutes=timeout_in_minutes,
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
    json_body: CodatDataContractsDatasetsBankAccount,
    allow_sync_on_push_complete: Union[Unset, None, bool] = True,
    timeout_in_minutes: Union[Unset, None, int] = UNSET,
) -> Optional[CodatDataContractsDatasetsBankAccountPushOperation]:
    """Posts a new bank account to the accounting package for a given company.

    Args:
        company_id (str):
        connection_id (str):
        allow_sync_on_push_complete (Union[Unset, None, bool]):  Default: True.
        timeout_in_minutes (Union[Unset, None, int]):
        json_body (CodatDataContractsDatasetsBankAccount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsBankAccountPushOperation
    """

    return sync_detailed(
        company_id=company_id,
        connection_id=connection_id,
        client=client,
        json_body=json_body,
        allow_sync_on_push_complete=allow_sync_on_push_complete,
        timeout_in_minutes=timeout_in_minutes,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatDataContractsDatasetsBankAccount,
    allow_sync_on_push_complete: Union[Unset, None, bool] = True,
    timeout_in_minutes: Union[Unset, None, int] = UNSET,
) -> Response[CodatDataContractsDatasetsBankAccountPushOperation]:
    """Posts a new bank account to the accounting package for a given company.

    Args:
        company_id (str):
        connection_id (str):
        allow_sync_on_push_complete (Union[Unset, None, bool]):  Default: True.
        timeout_in_minutes (Union[Unset, None, int]):
        json_body (CodatDataContractsDatasetsBankAccount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsBankAccountPushOperation]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        json_body=json_body,
        allow_sync_on_push_complete=allow_sync_on_push_complete,
        timeout_in_minutes=timeout_in_minutes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatDataContractsDatasetsBankAccount,
    allow_sync_on_push_complete: Union[Unset, None, bool] = True,
    timeout_in_minutes: Union[Unset, None, int] = UNSET,
) -> Optional[CodatDataContractsDatasetsBankAccountPushOperation]:
    """Posts a new bank account to the accounting package for a given company.

    Args:
        company_id (str):
        connection_id (str):
        allow_sync_on_push_complete (Union[Unset, None, bool]):  Default: True.
        timeout_in_minutes (Union[Unset, None, int]):
        json_body (CodatDataContractsDatasetsBankAccount):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsBankAccountPushOperation
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            connection_id=connection_id,
            client=client,
            json_body=json_body,
            allow_sync_on_push_complete=allow_sync_on_push_complete,
            timeout_in_minutes=timeout_in_minutes,
        )
    ).parsed
