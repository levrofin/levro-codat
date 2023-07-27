from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_contracts_datasets_attachments_dataset_attachment import (
    CodatDataContractsDatasetsAttachmentsDatasetAttachment,
)
from ...types import Response


def _get_kwargs(
    company_id: str,
    connection_id: str,
    direct_cost_id: str,
    attachment_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/companies/{companyId}/connections/{connectionId}/data/directCosts/{directCostId}/attachments/{attachmentId}".format(
            companyId=company_id,
            connectionId=connection_id,
            directCostId=direct_cost_id,
            attachmentId=attachment_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatDataContractsDatasetsAttachmentsDatasetAttachment]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataContractsDatasetsAttachmentsDatasetAttachment.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatDataContractsDatasetsAttachmentsDatasetAttachment]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    connection_id: str,
    direct_cost_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsDatasetsAttachmentsDatasetAttachment]:
    """Gets the specified direct cost attachment for a given company.

    Args:
        company_id (str):
        connection_id (str):
        direct_cost_id (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsAttachmentsDatasetAttachment]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        direct_cost_id=direct_cost_id,
        attachment_id=attachment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    connection_id: str,
    direct_cost_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsDatasetsAttachmentsDatasetAttachment]:
    """Gets the specified direct cost attachment for a given company.

    Args:
        company_id (str):
        connection_id (str):
        direct_cost_id (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsAttachmentsDatasetAttachment
    """

    return sync_detailed(
        company_id=company_id,
        connection_id=connection_id,
        direct_cost_id=direct_cost_id,
        attachment_id=attachment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    connection_id: str,
    direct_cost_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsDatasetsAttachmentsDatasetAttachment]:
    """Gets the specified direct cost attachment for a given company.

    Args:
        company_id (str):
        connection_id (str):
        direct_cost_id (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsAttachmentsDatasetAttachment]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        direct_cost_id=direct_cost_id,
        attachment_id=attachment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    connection_id: str,
    direct_cost_id: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsDatasetsAttachmentsDatasetAttachment]:
    """Gets the specified direct cost attachment for a given company.

    Args:
        company_id (str):
        connection_id (str):
        direct_cost_id (str):
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsAttachmentsDatasetAttachment
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            connection_id=connection_id,
            direct_cost_id=direct_cost_id,
            attachment_id=attachment_id,
            client=client,
        )
    ).parsed
