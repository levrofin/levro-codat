from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_public_api_models_data_data_set import CodatPublicApiModelsDataDataSet
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    data_type: str,
    *,
    connection_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["connectionId"] = connection_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": "/companies/{companyId}/data/queue/{dataType}".format(
            companyId=company_id,
            dataType=data_type,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatPublicApiModelsDataDataSet]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatPublicApiModelsDataDataSet.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatPublicApiModelsDataDataSet]:
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
    connection_id: Union[Unset, None, str] = UNSET,
) -> Response[CodatPublicApiModelsDataDataSet]:
    """Initiates the process of capturing a data snapshot of a specified type for a company

     Initiates the synchronisation for a specified data type

    Args:
        company_id (str):
        data_type (str):
        connection_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsDataDataSet]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        data_type=data_type,
        connection_id=connection_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    data_type: str,
    *,
    client: AuthenticatedClient,
    connection_id: Union[Unset, None, str] = UNSET,
) -> Optional[CodatPublicApiModelsDataDataSet]:
    """Initiates the process of capturing a data snapshot of a specified type for a company

     Initiates the synchronisation for a specified data type

    Args:
        company_id (str):
        data_type (str):
        connection_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatPublicApiModelsDataDataSet
    """

    return sync_detailed(
        company_id=company_id,
        data_type=data_type,
        client=client,
        connection_id=connection_id,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    data_type: str,
    *,
    client: AuthenticatedClient,
    connection_id: Union[Unset, None, str] = UNSET,
) -> Response[CodatPublicApiModelsDataDataSet]:
    """Initiates the process of capturing a data snapshot of a specified type for a company

     Initiates the synchronisation for a specified data type

    Args:
        company_id (str):
        data_type (str):
        connection_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsDataDataSet]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        data_type=data_type,
        connection_id=connection_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    data_type: str,
    *,
    client: AuthenticatedClient,
    connection_id: Union[Unset, None, str] = UNSET,
) -> Optional[CodatPublicApiModelsDataDataSet]:
    """Initiates the process of capturing a data snapshot of a specified type for a company

     Initiates the synchronisation for a specified data type

    Args:
        company_id (str):
        data_type (str):
        connection_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatPublicApiModelsDataDataSet
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            data_type=data_type,
            client=client,
            connection_id=connection_id,
        )
    ).parsed
