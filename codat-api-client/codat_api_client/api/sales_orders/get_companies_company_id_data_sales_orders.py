from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_contracts_datasets_sales_order_paged_response_model import (
    CodatDataContractsDatasetsSalesOrderPagedResponseModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    *,
    client: AuthenticatedClient,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
    query: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/companies/{companyId}/data/salesOrders".format(client.base_url, companyId=company_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["pageSize"] = page_size

    params["query"] = query

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
) -> Optional[CodatDataContractsDatasetsSalesOrderPagedResponseModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataContractsDatasetsSalesOrderPagedResponseModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[CodatDataContractsDatasetsSalesOrderPagedResponseModel]:
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
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
    query: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Response[CodatDataContractsDatasetsSalesOrderPagedResponseModel]:
    """
    Args:
        company_id (str):
        page (int):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 100.
        query (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsSalesOrderPagedResponseModel]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        client=client,
        page=page,
        page_size=page_size,
        query=query,
        order_by=order_by,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    *,
    client: AuthenticatedClient,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
    query: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Optional[CodatDataContractsDatasetsSalesOrderPagedResponseModel]:
    """
    Args:
        company_id (str):
        page (int):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 100.
        query (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsSalesOrderPagedResponseModel]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        page=page,
        page_size=page_size,
        query=query,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
    query: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Response[CodatDataContractsDatasetsSalesOrderPagedResponseModel]:
    """
    Args:
        company_id (str):
        page (int):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 100.
        query (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsSalesOrderPagedResponseModel]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        client=client,
        page=page,
        page_size=page_size,
        query=query,
        order_by=order_by,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: AuthenticatedClient,
    page: int = 1,
    page_size: Union[Unset, None, int] = 100,
    query: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, str] = UNSET,
) -> Optional[CodatDataContractsDatasetsSalesOrderPagedResponseModel]:
    """
    Args:
        company_id (str):
        page (int):  Default: 1.
        page_size (Union[Unset, None, int]):  Default: 100.
        query (Union[Unset, None, str]):
        order_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsSalesOrderPagedResponseModel]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            page=page,
            page_size=page_size,
            query=query,
            order_by=order_by,
        )
    ).parsed
