import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_contracts_datasets_aged_creditor_outstanding_i_collection_report import (
    CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    *,
    client: AuthenticatedClient,
    report_date: Union[Unset, None, datetime.datetime] = UNSET,
    number_of_periods: Union[Unset, None, int] = UNSET,
    period_length_days: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/companies/{companyId}/reports/agedCreditor".format(client.base_url, companyId=company_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_report_date: Union[Unset, None, str] = UNSET
    if not isinstance(report_date, Unset):
        json_report_date = report_date.isoformat() if report_date else None

    params["reportDate"] = json_report_date

    params["numberOfPeriods"] = number_of_periods

    params["periodLengthDays"] = period_length_days

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    report_date: Union[Unset, None, datetime.datetime] = UNSET,
    number_of_periods: Union[Unset, None, int] = UNSET,
    period_length_days: Union[Unset, None, int] = UNSET,
) -> Response[CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport]:
    """Gets the aged creditor report for a company.

    Args:
        company_id (str):
        report_date (Union[Unset, None, datetime.datetime]):
        number_of_periods (Union[Unset, None, int]):
        period_length_days (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        client=client,
        report_date=report_date,
        number_of_periods=number_of_periods,
        period_length_days=period_length_days,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    *,
    client: AuthenticatedClient,
    report_date: Union[Unset, None, datetime.datetime] = UNSET,
    number_of_periods: Union[Unset, None, int] = UNSET,
    period_length_days: Union[Unset, None, int] = UNSET,
) -> Optional[CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport]:
    """Gets the aged creditor report for a company.

    Args:
        company_id (str):
        report_date (Union[Unset, None, datetime.datetime]):
        number_of_periods (Union[Unset, None, int]):
        period_length_days (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        report_date=report_date,
        number_of_periods=number_of_periods,
        period_length_days=period_length_days,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    report_date: Union[Unset, None, datetime.datetime] = UNSET,
    number_of_periods: Union[Unset, None, int] = UNSET,
    period_length_days: Union[Unset, None, int] = UNSET,
) -> Response[CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport]:
    """Gets the aged creditor report for a company.

    Args:
        company_id (str):
        report_date (Union[Unset, None, datetime.datetime]):
        number_of_periods (Union[Unset, None, int]):
        period_length_days (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        client=client,
        report_date=report_date,
        number_of_periods=number_of_periods,
        period_length_days=period_length_days,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: AuthenticatedClient,
    report_date: Union[Unset, None, datetime.datetime] = UNSET,
    number_of_periods: Union[Unset, None, int] = UNSET,
    period_length_days: Union[Unset, None, int] = UNSET,
) -> Optional[CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport]:
    """Gets the aged creditor report for a company.

    Args:
        company_id (str):
        report_date (Union[Unset, None, datetime.datetime]):
        number_of_periods (Union[Unset, None, int]):
        period_length_days (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            report_date=report_date,
            number_of_periods=number_of_periods,
            period_length_days=period_length_days,
        )
    ).parsed
