from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_contracts_push_push_option import CodatDataContractsPushPushOption
from ...types import Response


def _get_kwargs(
    company_id: str,
    connection_id: str,
    data_type: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/companies/{companyId}/connections/{connectionId}/dataTypes/{dataType}/options/PUT".format(
            companyId=company_id,
            connectionId=connection_id,
            dataType=data_type,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatDataContractsPushPushOption]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataContractsPushPushOption.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatDataContractsPushPushOption]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    connection_id: str,
    data_type: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsPushPushOption]:
    """Gets the PUT push options for the given data type

    Args:
        company_id (str):
        connection_id (str):
        data_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsPushPushOption]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        data_type=data_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    connection_id: str,
    data_type: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsPushPushOption]:
    """Gets the PUT push options for the given data type

    Args:
        company_id (str):
        connection_id (str):
        data_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsPushPushOption
    """

    return sync_detailed(
        company_id=company_id,
        connection_id=connection_id,
        data_type=data_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    connection_id: str,
    data_type: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsPushPushOption]:
    """Gets the PUT push options for the given data type

    Args:
        company_id (str):
        connection_id (str):
        data_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsPushPushOption]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        data_type=data_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    connection_id: str,
    data_type: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsPushPushOption]:
    """Gets the PUT push options for the given data type

    Args:
        company_id (str):
        connection_id (str):
        data_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsPushPushOption
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            connection_id=connection_id,
            data_type=data_type,
            client=client,
        )
    ).parsed
