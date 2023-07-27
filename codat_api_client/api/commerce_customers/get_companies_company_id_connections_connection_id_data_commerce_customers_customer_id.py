from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_contracts_datasets_commerce_customer import CodatDataContractsDatasetsCommerceCustomer
from ...types import Response


def _get_kwargs(
    company_id: str,
    connection_id: str,
    customer_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/companies/{companyId}/connections/{connectionId}/data/commerce-customers/{customerId}".format(
            companyId=company_id,
            connectionId=connection_id,
            customerId=customer_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatDataContractsDatasetsCommerceCustomer]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataContractsDatasetsCommerceCustomer.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatDataContractsDatasetsCommerceCustomer]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    connection_id: str,
    customer_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsDatasetsCommerceCustomer]:
    """Gets the specified commerce customer for a given company

    Args:
        company_id (str):
        connection_id (str):
        customer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsCommerceCustomer]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        customer_id=customer_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    connection_id: str,
    customer_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsDatasetsCommerceCustomer]:
    """Gets the specified commerce customer for a given company

    Args:
        company_id (str):
        connection_id (str):
        customer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsCommerceCustomer
    """

    return sync_detailed(
        company_id=company_id,
        connection_id=connection_id,
        customer_id=customer_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    connection_id: str,
    customer_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsDatasetsCommerceCustomer]:
    """Gets the specified commerce customer for a given company

    Args:
        company_id (str):
        connection_id (str):
        customer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsCommerceCustomer]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        customer_id=customer_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    connection_id: str,
    customer_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsDatasetsCommerceCustomer]:
    """Gets the specified commerce customer for a given company

    Args:
        company_id (str):
        connection_id (str):
        customer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsCommerceCustomer
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            connection_id=connection_id,
            customer_id=customer_id,
            client=client,
        )
    ).parsed
