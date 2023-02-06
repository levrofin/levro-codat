from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_contracts_datasets_journal_entry import CodatDataContractsDatasetsJournalEntry
from ...types import Response


def _get_kwargs(
    company_id: str,
    journal_entry_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/companies/{companyId}/data/journalEntries/{journalEntryId}".format(
        client.base_url, companyId=company_id, journalEntryId=journal_entry_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[CodatDataContractsDatasetsJournalEntry]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataContractsDatasetsJournalEntry.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[CodatDataContractsDatasetsJournalEntry]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    journal_entry_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsDatasetsJournalEntry]:
    """Gets a single JournalEntry corresponding to the supplied Id

    Args:
        company_id (str):
        journal_entry_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsJournalEntry]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        journal_entry_id=journal_entry_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    journal_entry_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsDatasetsJournalEntry]:
    """Gets a single JournalEntry corresponding to the supplied Id

    Args:
        company_id (str):
        journal_entry_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsJournalEntry]
    """

    return sync_detailed(
        company_id=company_id,
        journal_entry_id=journal_entry_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    journal_entry_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsDatasetsJournalEntry]:
    """Gets a single JournalEntry corresponding to the supplied Id

    Args:
        company_id (str):
        journal_entry_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsJournalEntry]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        journal_entry_id=journal_entry_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    journal_entry_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsDatasetsJournalEntry]:
    """Gets a single JournalEntry corresponding to the supplied Id

    Args:
        company_id (str):
        journal_entry_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsJournalEntry]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            journal_entry_id=journal_entry_id,
            client=client,
        )
    ).parsed
