from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_contracts_datasets_credit_note import CodatDataContractsDatasetsCreditNote
from ...models.codat_data_contracts_datasets_credit_note_push_operation import (
    CodatDataContractsDatasetsCreditNotePushOperation,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    connection_id: str,
    credit_note_id: str,
    *,
    json_body: CodatDataContractsDatasetsCreditNote,
    timeout_in_minutes: Union[Unset, None, int] = UNSET,
    force_update: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    params["timeoutInMinutes"] = timeout_in_minutes

    params["forceUpdate"] = force_update

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/companies/{companyId}/connections/{connectionId}/push/creditNotes/{creditNoteId}".format(
            companyId=company_id,
            connectionId=connection_id,
            creditNoteId=credit_note_id,
        ),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatDataContractsDatasetsCreditNotePushOperation]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataContractsDatasetsCreditNotePushOperation.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatDataContractsDatasetsCreditNotePushOperation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    connection_id: str,
    credit_note_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatDataContractsDatasetsCreditNote,
    timeout_in_minutes: Union[Unset, None, int] = UNSET,
    force_update: Union[Unset, None, bool] = False,
) -> Response[CodatDataContractsDatasetsCreditNotePushOperation]:
    """Posts an updated credit note to the accounting package for a given company.

    Args:
        company_id (str):
        connection_id (str):
        credit_note_id (str):
        timeout_in_minutes (Union[Unset, None, int]):
        force_update (Union[Unset, None, bool]):
        json_body (CodatDataContractsDatasetsCreditNote):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsCreditNotePushOperation]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        credit_note_id=credit_note_id,
        json_body=json_body,
        timeout_in_minutes=timeout_in_minutes,
        force_update=force_update,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    connection_id: str,
    credit_note_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatDataContractsDatasetsCreditNote,
    timeout_in_minutes: Union[Unset, None, int] = UNSET,
    force_update: Union[Unset, None, bool] = False,
) -> Optional[CodatDataContractsDatasetsCreditNotePushOperation]:
    """Posts an updated credit note to the accounting package for a given company.

    Args:
        company_id (str):
        connection_id (str):
        credit_note_id (str):
        timeout_in_minutes (Union[Unset, None, int]):
        force_update (Union[Unset, None, bool]):
        json_body (CodatDataContractsDatasetsCreditNote):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsCreditNotePushOperation
    """

    return sync_detailed(
        company_id=company_id,
        connection_id=connection_id,
        credit_note_id=credit_note_id,
        client=client,
        json_body=json_body,
        timeout_in_minutes=timeout_in_minutes,
        force_update=force_update,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    connection_id: str,
    credit_note_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatDataContractsDatasetsCreditNote,
    timeout_in_minutes: Union[Unset, None, int] = UNSET,
    force_update: Union[Unset, None, bool] = False,
) -> Response[CodatDataContractsDatasetsCreditNotePushOperation]:
    """Posts an updated credit note to the accounting package for a given company.

    Args:
        company_id (str):
        connection_id (str):
        credit_note_id (str):
        timeout_in_minutes (Union[Unset, None, int]):
        force_update (Union[Unset, None, bool]):
        json_body (CodatDataContractsDatasetsCreditNote):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsCreditNotePushOperation]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        credit_note_id=credit_note_id,
        json_body=json_body,
        timeout_in_minutes=timeout_in_minutes,
        force_update=force_update,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    connection_id: str,
    credit_note_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatDataContractsDatasetsCreditNote,
    timeout_in_minutes: Union[Unset, None, int] = UNSET,
    force_update: Union[Unset, None, bool] = False,
) -> Optional[CodatDataContractsDatasetsCreditNotePushOperation]:
    """Posts an updated credit note to the accounting package for a given company.

    Args:
        company_id (str):
        connection_id (str):
        credit_note_id (str):
        timeout_in_minutes (Union[Unset, None, int]):
        force_update (Union[Unset, None, bool]):
        json_body (CodatDataContractsDatasetsCreditNote):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsCreditNotePushOperation
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            connection_id=connection_id,
            credit_note_id=credit_note_id,
            client=client,
            json_body=json_body,
            timeout_in_minutes=timeout_in_minutes,
            force_update=force_update,
        )
    ).parsed
