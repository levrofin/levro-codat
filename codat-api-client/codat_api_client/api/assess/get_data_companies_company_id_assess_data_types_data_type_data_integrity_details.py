from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_integrity_contracts_details_transaction_details_paged_response import (
    CodatDataIntegrityContractsDetailsTransactionDetailsPagedResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    data_type: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, None, int] = 1,
    query: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/data/companies/{companyId}/assess/dataTypes/{dataType}/dataIntegrity/details".format(
        client.base_url, companyId=company_id, dataType=data_type
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["query"] = query

    params["pageSize"] = page_size

    params["orderBy"] = order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[CodatDataIntegrityContractsDetailsTransactionDetailsPagedResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataIntegrityContractsDetailsTransactionDetailsPagedResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[CodatDataIntegrityContractsDetailsTransactionDetailsPagedResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    data_type: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, None, int] = 1,
    query: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Response[CodatDataIntegrityContractsDetailsTransactionDetailsPagedResponse]:
    """Gets record-by-record match results for a given company and datatype, optionally restricted by a
    Codat query string.

    Args:
        company_id (str):
        data_type (str):
        page (Union[Unset, None, int]):  Default: 1.
        query (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataIntegrityContractsDetailsTransactionDetailsPagedResponse]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        data_type=data_type,
        client=client,
        page=page,
        query=query,
        page_size=page_size,
        order_by=order_by,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    data_type: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, None, int] = 1,
    query: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Optional[CodatDataIntegrityContractsDetailsTransactionDetailsPagedResponse]:
    """Gets record-by-record match results for a given company and datatype, optionally restricted by a
    Codat query string.

    Args:
        company_id (str):
        data_type (str):
        page (Union[Unset, None, int]):  Default: 1.
        query (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataIntegrityContractsDetailsTransactionDetailsPagedResponse]
    """

    return sync_detailed(
        company_id=company_id,
        data_type=data_type,
        client=client,
        page=page,
        query=query,
        page_size=page_size,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    data_type: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, None, int] = 1,
    query: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Response[CodatDataIntegrityContractsDetailsTransactionDetailsPagedResponse]:
    """Gets record-by-record match results for a given company and datatype, optionally restricted by a
    Codat query string.

    Args:
        company_id (str):
        data_type (str):
        page (Union[Unset, None, int]):  Default: 1.
        query (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataIntegrityContractsDetailsTransactionDetailsPagedResponse]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        data_type=data_type,
        client=client,
        page=page,
        query=query,
        page_size=page_size,
        order_by=order_by,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    data_type: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, None, int] = 1,
    query: Union[Unset, None, str] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Optional[CodatDataIntegrityContractsDetailsTransactionDetailsPagedResponse]:
    """Gets record-by-record match results for a given company and datatype, optionally restricted by a
    Codat query string.

    Args:
        company_id (str):
        data_type (str):
        page (Union[Unset, None, int]):  Default: 1.
        query (Union[Unset, None, str]):
        page_size (Union[Unset, None, int]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataIntegrityContractsDetailsTransactionDetailsPagedResponse]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            data_type=data_type,
            client=client,
            page=page,
            query=query,
            page_size=page_size,
            order_by=order_by,
        )
    ).parsed
