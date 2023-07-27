from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_contracts_datasets_sales_order import CodatDataContractsDatasetsSalesOrder
from ...types import Response


def _get_kwargs(
    company_id: str,
    sales_order_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/companies/{companyId}/data/salesOrders/{salesOrderId}".format(
            companyId=company_id,
            salesOrderId=sales_order_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatDataContractsDatasetsSalesOrder]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataContractsDatasetsSalesOrder.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatDataContractsDatasetsSalesOrder]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    sales_order_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsDatasetsSalesOrder]:
    """
    Args:
        company_id (str):
        sales_order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsSalesOrder]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        sales_order_id=sales_order_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    sales_order_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsDatasetsSalesOrder]:
    """
    Args:
        company_id (str):
        sales_order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsSalesOrder
    """

    return sync_detailed(
        company_id=company_id,
        sales_order_id=sales_order_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    sales_order_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsDatasetsSalesOrder]:
    """
    Args:
        company_id (str):
        sales_order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsSalesOrder]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        sales_order_id=sales_order_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    sales_order_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsDatasetsSalesOrder]:
    """
    Args:
        company_id (str):
        sales_order_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsSalesOrder
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            sales_order_id=sales_order_id,
            client=client,
        )
    ).parsed
