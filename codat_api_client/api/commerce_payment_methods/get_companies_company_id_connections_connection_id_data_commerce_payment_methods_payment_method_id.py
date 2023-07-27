from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_contracts_datasets_commerce_payment_method import (
    CodatDataContractsDatasetsCommercePaymentMethod,
)
from ...types import Response


def _get_kwargs(
    company_id: str,
    connection_id: str,
    payment_method_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/companies/{companyId}/connections/{connectionId}/data/commerce-paymentMethods/{paymentMethodId}".format(
            companyId=company_id,
            connectionId=connection_id,
            paymentMethodId=payment_method_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatDataContractsDatasetsCommercePaymentMethod]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataContractsDatasetsCommercePaymentMethod.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatDataContractsDatasetsCommercePaymentMethod]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    connection_id: str,
    payment_method_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsDatasetsCommercePaymentMethod]:
    """Gets the details of an individual payment method.

    Args:
        company_id (str):
        connection_id (str):
        payment_method_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsCommercePaymentMethod]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        payment_method_id=payment_method_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    connection_id: str,
    payment_method_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsDatasetsCommercePaymentMethod]:
    """Gets the details of an individual payment method.

    Args:
        company_id (str):
        connection_id (str):
        payment_method_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsCommercePaymentMethod
    """

    return sync_detailed(
        company_id=company_id,
        connection_id=connection_id,
        payment_method_id=payment_method_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    connection_id: str,
    payment_method_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsDatasetsCommercePaymentMethod]:
    """Gets the details of an individual payment method.

    Args:
        company_id (str):
        connection_id (str):
        payment_method_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsCommercePaymentMethod]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        payment_method_id=payment_method_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    connection_id: str,
    payment_method_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsDatasetsCommercePaymentMethod]:
    """Gets the details of an individual payment method.

    Args:
        company_id (str):
        connection_id (str):
        payment_method_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsCommercePaymentMethod
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            connection_id=connection_id,
            payment_method_id=payment_method_id,
            client=client,
        )
    ).parsed
