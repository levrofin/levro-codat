import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_standard_reporting_contracts_report import CodatStandardReportingContractsReport
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
    report_date: datetime.datetime,
    period_length: int,
    number_of_periods: int,
    include_display_names: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/data/companies/{companyId}/connections/{connectionId}/assess/enhancedProfitAndLoss".format(
        client.base_url, companyId=company_id, connectionId=connection_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_report_date = report_date.isoformat()

    params["reportDate"] = json_report_date

    params["periodLength"] = period_length

    params["numberOfPeriods"] = number_of_periods

    params["includeDisplayNames"] = include_display_names

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[CodatStandardReportingContractsReport]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatStandardReportingContractsReport.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[CodatStandardReportingContractsReport]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
    report_date: datetime.datetime,
    period_length: int,
    number_of_periods: int,
    include_display_names: Union[Unset, None, bool] = False,
) -> Response[CodatStandardReportingContractsReport]:
    """Gets a fully categorized profit and loss statement for a given company, over one or more period(s).

    Args:
        company_id (str):
        connection_id (str):
        report_date (datetime.datetime):
        period_length (int):
        number_of_periods (int):
        include_display_names (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatStandardReportingContractsReport]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        client=client,
        report_date=report_date,
        period_length=period_length,
        number_of_periods=number_of_periods,
        include_display_names=include_display_names,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
    report_date: datetime.datetime,
    period_length: int,
    number_of_periods: int,
    include_display_names: Union[Unset, None, bool] = False,
) -> Optional[CodatStandardReportingContractsReport]:
    """Gets a fully categorized profit and loss statement for a given company, over one or more period(s).

    Args:
        company_id (str):
        connection_id (str):
        report_date (datetime.datetime):
        period_length (int):
        number_of_periods (int):
        include_display_names (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatStandardReportingContractsReport]
    """

    return sync_detailed(
        company_id=company_id,
        connection_id=connection_id,
        client=client,
        report_date=report_date,
        period_length=period_length,
        number_of_periods=number_of_periods,
        include_display_names=include_display_names,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
    report_date: datetime.datetime,
    period_length: int,
    number_of_periods: int,
    include_display_names: Union[Unset, None, bool] = False,
) -> Response[CodatStandardReportingContractsReport]:
    """Gets a fully categorized profit and loss statement for a given company, over one or more period(s).

    Args:
        company_id (str):
        connection_id (str):
        report_date (datetime.datetime):
        period_length (int):
        number_of_periods (int):
        include_display_names (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatStandardReportingContractsReport]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        client=client,
        report_date=report_date,
        period_length=period_length,
        number_of_periods=number_of_periods,
        include_display_names=include_display_names,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
    report_date: datetime.datetime,
    period_length: int,
    number_of_periods: int,
    include_display_names: Union[Unset, None, bool] = False,
) -> Optional[CodatStandardReportingContractsReport]:
    """Gets a fully categorized profit and loss statement for a given company, over one or more period(s).

    Args:
        company_id (str):
        connection_id (str):
        report_date (datetime.datetime):
        period_length (int):
        number_of_periods (int):
        include_display_names (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatStandardReportingContractsReport]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            connection_id=connection_id,
            client=client,
            report_date=report_date,
            period_length=period_length,
            number_of_periods=number_of_periods,
            include_display_names=include_display_names,
        )
    ).parsed
