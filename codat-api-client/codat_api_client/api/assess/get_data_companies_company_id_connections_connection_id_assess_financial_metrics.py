import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_assess_data_contracts_financials_metrics_financial_metrics_data_set import (
    CodatAssessDataContractsFinancialsMetricsFinancialMetricsDataSet,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
    report_date: datetime.datetime,
    period_length: int,
    number_of_periods: int,
    show_metric_inputs: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/data/companies/{companyId}/connections/{connectionId}/assess/financialMetrics".format(
        client.base_url, companyId=company_id, connectionId=connection_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_report_date = report_date.isoformat()

    params["reportDate"] = json_report_date

    params["periodLength"] = period_length

    params["numberOfPeriods"] = number_of_periods

    params["showMetricInputs"] = show_metric_inputs

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
) -> Optional[CodatAssessDataContractsFinancialsMetricsFinancialMetricsDataSet]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatAssessDataContractsFinancialsMetricsFinancialMetricsDataSet.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[CodatAssessDataContractsFinancialsMetricsFinancialMetricsDataSet]:
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
    show_metric_inputs: Union[Unset, None, bool] = False,
) -> Response[CodatAssessDataContractsFinancialsMetricsFinancialMetricsDataSet]:
    """Gets all the available financial metrics for a given company, over one or more periods.

    Args:
        company_id (str):
        connection_id (str):
        report_date (datetime.datetime):
        period_length (int):
        number_of_periods (int):
        show_metric_inputs (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatAssessDataContractsFinancialsMetricsFinancialMetricsDataSet]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        client=client,
        report_date=report_date,
        period_length=period_length,
        number_of_periods=number_of_periods,
        show_metric_inputs=show_metric_inputs,
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
    show_metric_inputs: Union[Unset, None, bool] = False,
) -> Optional[CodatAssessDataContractsFinancialsMetricsFinancialMetricsDataSet]:
    """Gets all the available financial metrics for a given company, over one or more periods.

    Args:
        company_id (str):
        connection_id (str):
        report_date (datetime.datetime):
        period_length (int):
        number_of_periods (int):
        show_metric_inputs (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatAssessDataContractsFinancialsMetricsFinancialMetricsDataSet]
    """

    return sync_detailed(
        company_id=company_id,
        connection_id=connection_id,
        client=client,
        report_date=report_date,
        period_length=period_length,
        number_of_periods=number_of_periods,
        show_metric_inputs=show_metric_inputs,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
    report_date: datetime.datetime,
    period_length: int,
    number_of_periods: int,
    show_metric_inputs: Union[Unset, None, bool] = False,
) -> Response[CodatAssessDataContractsFinancialsMetricsFinancialMetricsDataSet]:
    """Gets all the available financial metrics for a given company, over one or more periods.

    Args:
        company_id (str):
        connection_id (str):
        report_date (datetime.datetime):
        period_length (int):
        number_of_periods (int):
        show_metric_inputs (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatAssessDataContractsFinancialsMetricsFinancialMetricsDataSet]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        client=client,
        report_date=report_date,
        period_length=period_length,
        number_of_periods=number_of_periods,
        show_metric_inputs=show_metric_inputs,
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
    show_metric_inputs: Union[Unset, None, bool] = False,
) -> Optional[CodatAssessDataContractsFinancialsMetricsFinancialMetricsDataSet]:
    """Gets all the available financial metrics for a given company, over one or more periods.

    Args:
        company_id (str):
        connection_id (str):
        report_date (datetime.datetime):
        period_length (int):
        number_of_periods (int):
        show_metric_inputs (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatAssessDataContractsFinancialsMetricsFinancialMetricsDataSet]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            connection_id=connection_id,
            client=client,
            report_date=report_date,
            period_length=period_length,
            number_of_periods=number_of_periods,
            show_metric_inputs=show_metric_inputs,
        )
    ).parsed
