from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_contracts_datasets_invoice import CodatDataContractsDatasetsInvoice
from ...models.codat_data_contracts_datasets_invoice_push_operation import (
    CodatDataContractsDatasetsInvoicePushOperation,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    connection_id: str,
    invoice_id: str,
    *,
    json_body: CodatDataContractsDatasetsInvoice,
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
        "url": "/companies/{companyId}/connections/{connectionId}/push/invoices/{invoiceId}".format(
            companyId=company_id,
            connectionId=connection_id,
            invoiceId=invoice_id,
        ),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatDataContractsDatasetsInvoicePushOperation]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataContractsDatasetsInvoicePushOperation.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatDataContractsDatasetsInvoicePushOperation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    connection_id: str,
    invoice_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatDataContractsDatasetsInvoice,
    timeout_in_minutes: Union[Unset, None, int] = UNSET,
    force_update: Union[Unset, None, bool] = False,
) -> Response[CodatDataContractsDatasetsInvoicePushOperation]:
    """Posts an updated invoice to the accounting package for a given company.

    Args:
        company_id (str):
        connection_id (str):
        invoice_id (str):
        timeout_in_minutes (Union[Unset, None, int]):
        force_update (Union[Unset, None, bool]):
        json_body (CodatDataContractsDatasetsInvoice):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsInvoicePushOperation]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        invoice_id=invoice_id,
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
    invoice_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatDataContractsDatasetsInvoice,
    timeout_in_minutes: Union[Unset, None, int] = UNSET,
    force_update: Union[Unset, None, bool] = False,
) -> Optional[CodatDataContractsDatasetsInvoicePushOperation]:
    """Posts an updated invoice to the accounting package for a given company.

    Args:
        company_id (str):
        connection_id (str):
        invoice_id (str):
        timeout_in_minutes (Union[Unset, None, int]):
        force_update (Union[Unset, None, bool]):
        json_body (CodatDataContractsDatasetsInvoice):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsInvoicePushOperation
    """

    return sync_detailed(
        company_id=company_id,
        connection_id=connection_id,
        invoice_id=invoice_id,
        client=client,
        json_body=json_body,
        timeout_in_minutes=timeout_in_minutes,
        force_update=force_update,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    connection_id: str,
    invoice_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatDataContractsDatasetsInvoice,
    timeout_in_minutes: Union[Unset, None, int] = UNSET,
    force_update: Union[Unset, None, bool] = False,
) -> Response[CodatDataContractsDatasetsInvoicePushOperation]:
    """Posts an updated invoice to the accounting package for a given company.

    Args:
        company_id (str):
        connection_id (str):
        invoice_id (str):
        timeout_in_minutes (Union[Unset, None, int]):
        force_update (Union[Unset, None, bool]):
        json_body (CodatDataContractsDatasetsInvoice):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsInvoicePushOperation]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        invoice_id=invoice_id,
        json_body=json_body,
        timeout_in_minutes=timeout_in_minutes,
        force_update=force_update,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    connection_id: str,
    invoice_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatDataContractsDatasetsInvoice,
    timeout_in_minutes: Union[Unset, None, int] = UNSET,
    force_update: Union[Unset, None, bool] = False,
) -> Optional[CodatDataContractsDatasetsInvoicePushOperation]:
    """Posts an updated invoice to the accounting package for a given company.

    Args:
        company_id (str):
        connection_id (str):
        invoice_id (str):
        timeout_in_minutes (Union[Unset, None, int]):
        force_update (Union[Unset, None, bool]):
        json_body (CodatDataContractsDatasetsInvoice):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatDataContractsDatasetsInvoicePushOperation
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            connection_id=connection_id,
            invoice_id=invoice_id,
            client=client,
            json_body=json_body,
            timeout_in_minutes=timeout_in_minutes,
            force_update=force_update,
        )
    ).parsed
