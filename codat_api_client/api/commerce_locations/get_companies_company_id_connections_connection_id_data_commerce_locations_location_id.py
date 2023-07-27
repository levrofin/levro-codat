from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_contracts_datasets_commerce_location import CodatDataContractsDatasetsCommerceLocation
from ...types import Response


def _get_kwargs(
    company_id: str,
    connection_id: str,
    location_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/companies/{companyId}/connections/{connectionId}/data/commerce-locations/{locationId}".format(
            companyId=company_id,
            connectionId=connection_id,
            locationId=location_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatDataContractsDatasetsCommerceLocation]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataContractsDatasetsCommerceLocation.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatDataContractsDatasetsCommerceLocation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    connection_id: str,
    location_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsDatasetsCommerceLocation]:
    """Gets the specified commerce location for a given company

    Args:
        company_id (str):
        connection_id (str):
        location_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsCommerceLocation]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        location_id=location_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    connection_id: str,
    location_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsDatasetsCommerceLocation]:
    """Gets the specified commerce location for a given company

    Args:
        company_id (str):
        connection_id (str):
        location_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsCommerceLocation
    """

    return sync_detailed(
        company_id=company_id,
        connection_id=connection_id,
        location_id=location_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    connection_id: str,
    location_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsDatasetsCommerceLocation]:
    """Gets the specified commerce location for a given company

    Args:
        company_id (str):
        connection_id (str):
        location_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsCommerceLocation]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        location_id=location_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    connection_id: str,
    location_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsDatasetsCommerceLocation]:
    """Gets the specified commerce location for a given company

    Args:
        company_id (str):
        connection_id (str):
        location_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsCommerceLocation
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            connection_id=connection_id,
            location_id=location_id,
            client=client,
        )
    ).parsed
