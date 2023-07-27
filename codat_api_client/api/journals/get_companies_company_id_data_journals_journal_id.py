from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_contracts_datasets_journal import CodatDataContractsDatasetsJournal
from ...types import Response


def _get_kwargs(
    company_id: str,
    journal_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/companies/{companyId}/data/journals/{journalId}".format(
            companyId=company_id,
            journalId=journal_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatDataContractsDatasetsJournal]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataContractsDatasetsJournal.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatDataContractsDatasetsJournal]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    journal_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsDatasetsJournal]:
    """Gets a single journal corresponding to the supplied Id

    Args:
        company_id (str):
        journal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsJournal]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        journal_id=journal_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    journal_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsDatasetsJournal]:
    """Gets a single journal corresponding to the supplied Id

    Args:
        company_id (str):
        journal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsJournal
    """

    return sync_detailed(
        company_id=company_id,
        journal_id=journal_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    journal_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsDatasetsJournal]:
    """Gets a single journal corresponding to the supplied Id

    Args:
        company_id (str):
        journal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsJournal]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        journal_id=journal_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    journal_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsDatasetsJournal]:
    """Gets a single journal corresponding to the supplied Id

    Args:
        company_id (str):
        journal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsJournal
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            journal_id=journal_id,
            client=client,
        )
    ).parsed
