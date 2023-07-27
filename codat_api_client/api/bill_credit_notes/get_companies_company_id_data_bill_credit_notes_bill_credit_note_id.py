from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_contracts_datasets_bill_credit_note import CodatDataContractsDatasetsBillCreditNote
from ...types import Response


def _get_kwargs(
    company_id: str,
    bill_credit_note_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/companies/{companyId}/data/billCreditNotes/{billCreditNoteId}".format(
            companyId=company_id,
            billCreditNoteId=bill_credit_note_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatDataContractsDatasetsBillCreditNote]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataContractsDatasetsBillCreditNote.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatDataContractsDatasetsBillCreditNote]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    bill_credit_note_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsDatasetsBillCreditNote]:
    """Gets a single billCreditNote corresponding to the supplied Id

    Args:
        company_id (str):
        bill_credit_note_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsBillCreditNote]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        bill_credit_note_id=bill_credit_note_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    bill_credit_note_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsDatasetsBillCreditNote]:
    """Gets a single billCreditNote corresponding to the supplied Id

    Args:
        company_id (str):
        bill_credit_note_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsBillCreditNote
    """

    return sync_detailed(
        company_id=company_id,
        bill_credit_note_id=bill_credit_note_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    bill_credit_note_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatDataContractsDatasetsBillCreditNote]:
    """Gets a single billCreditNote corresponding to the supplied Id

    Args:
        company_id (str):
        bill_credit_note_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsBillCreditNote]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        bill_credit_note_id=bill_credit_note_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    bill_credit_note_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatDataContractsDatasetsBillCreditNote]:
    """Gets a single billCreditNote corresponding to the supplied Id

    Args:
        company_id (str):
        bill_credit_note_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsBillCreditNote
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            bill_credit_note_id=bill_credit_note_id,
            client=client,
        )
    ).parsed
