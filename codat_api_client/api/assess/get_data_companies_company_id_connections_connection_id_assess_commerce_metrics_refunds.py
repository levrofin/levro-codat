import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_assess_data_contracts_commerce_metrics_period_unit import (
    CodatAssessDataContractsCommerceMetricsPeriodUnit,
)
from ...models.codat_standard_reporting_contracts_report import CodatStandardReportingContractsReport
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    connection_id: str,
    *,
    report_date: datetime.datetime,
    period_length: int,
    number_of_periods: int,
    period_unit: CodatAssessDataContractsCommerceMetricsPeriodUnit,
    include_display_names: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_report_date = report_date.isoformat()

    params["reportDate"] = json_report_date

    params["periodLength"] = period_length

    params["numberOfPeriods"] = number_of_periods

    json_period_unit = period_unit.value

    params["periodUnit"] = json_period_unit

    params["includeDisplayNames"] = include_display_names

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/data/companies/{companyId}/connections/{connectionId}/assess/commerceMetrics/refunds".format(
            companyId=company_id,
            connectionId=connection_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatStandardReportingContractsReport]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatStandardReportingContractsReport.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatStandardReportingContractsReport]:
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
    period_unit: CodatAssessDataContractsCommerceMetricsPeriodUnit,
    include_display_names: Union[Unset, None, bool] = False,
) -> Response[CodatStandardReportingContractsReport]:
    """Gets the refunds information for a specific company connection, over one or more periods of time.

    Args:
        company_id (str):
        connection_id (str):
        report_date (datetime.datetime):
        period_length (int):
        number_of_periods (int):
        period_unit (CodatAssessDataContractsCommerceMetricsPeriodUnit):
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
        report_date=report_date,
        period_length=period_length,
        number_of_periods=number_of_periods,
        period_unit=period_unit,
        include_display_names=include_display_names,
    )

    response = client.get_httpx_client().request(
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
    period_unit: CodatAssessDataContractsCommerceMetricsPeriodUnit,
    include_display_names: Union[Unset, None, bool] = False,
) -> Optional[CodatStandardReportingContractsReport]:
    """Gets the refunds information for a specific company connection, over one or more periods of time.

    Args:
        company_id (str):
        connection_id (str):
        report_date (datetime.datetime):
        period_length (int):
        number_of_periods (int):
        period_unit (CodatAssessDataContractsCommerceMetricsPeriodUnit):
        include_display_names (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatStandardReportingContractsReport
    """

    return sync_detailed(
        company_id=company_id,
        connection_id=connection_id,
        client=client,
        report_date=report_date,
        period_length=period_length,
        number_of_periods=number_of_periods,
        period_unit=period_unit,
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
    period_unit: CodatAssessDataContractsCommerceMetricsPeriodUnit,
    include_display_names: Union[Unset, None, bool] = False,
) -> Response[CodatStandardReportingContractsReport]:
    """Gets the refunds information for a specific company connection, over one or more periods of time.

    Args:
        company_id (str):
        connection_id (str):
        report_date (datetime.datetime):
        period_length (int):
        number_of_periods (int):
        period_unit (CodatAssessDataContractsCommerceMetricsPeriodUnit):
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
        report_date=report_date,
        period_length=period_length,
        number_of_periods=number_of_periods,
        period_unit=period_unit,
        include_display_names=include_display_names,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
    report_date: datetime.datetime,
    period_length: int,
    number_of_periods: int,
    period_unit: CodatAssessDataContractsCommerceMetricsPeriodUnit,
    include_display_names: Union[Unset, None, bool] = False,
) -> Optional[CodatStandardReportingContractsReport]:
    """Gets the refunds information for a specific company connection, over one or more periods of time.

    Args:
        company_id (str):
        connection_id (str):
        report_date (datetime.datetime):
        period_length (int):
        number_of_periods (int):
        period_unit (CodatAssessDataContractsCommerceMetricsPeriodUnit):
        include_display_names (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatStandardReportingContractsReport
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            connection_id=connection_id,
            client=client,
            report_date=report_date,
            period_length=period_length,
            number_of_periods=number_of_periods,
            period_unit=period_unit,
            include_display_names=include_display_names,
        )
    ).parsed
