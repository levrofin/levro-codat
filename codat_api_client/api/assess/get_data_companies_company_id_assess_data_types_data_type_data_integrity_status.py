from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_integrity_contracts_metadata_match_metadata_response import (
    CodatDataIntegrityContractsMetadataMatchMetadataResponse,
)
from ...types import Response


def _get_kwargs(
    company_id: str,
    data_type: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/data/companies/{companyId}/assess/dataTypes/{dataType}/dataIntegrity/status".format(
            companyId=company_id,
            dataType=data_type,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatDataIntegrityContractsMetadataMatchMetadataResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataIntegrityContractsMetadataMatchMetadataResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatDataIntegrityContractsMetadataMatchMetadataResponse]:
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
) -> Response[CodatDataIntegrityContractsMetadataMatchMetadataResponse]:
    """Gets match status for a given company and datatype.

    Args:
        company_id (str):
        data_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataIntegrityContractsMetadataMatchMetadataResponse]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        data_type=data_type,
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
) -> Optional[CodatDataIntegrityContractsMetadataMatchMetadataResponse]:
    """Gets match status for a given company and datatype.

    Args:
        company_id (str):
        data_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataIntegrityContractsMetadataMatchMetadataResponse
    """

    return sync_detailed(
        company_id=company_id,
        data_type=data_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    data_type: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataIntegrityContractsMetadataMatchMetadataResponse]:
    """Gets match status for a given company and datatype.

    Args:
        company_id (str):
        data_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataIntegrityContractsMetadataMatchMetadataResponse]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        data_type=data_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    data_type: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataIntegrityContractsMetadataMatchMetadataResponse]:
    """Gets match status for a given company and datatype.

    Args:
        company_id (str):
        data_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataIntegrityContractsMetadataMatchMetadataResponse
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            data_type=data_type,
            client=client,
        )
    ).parsed
