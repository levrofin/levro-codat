import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_public_api_models_data_cash_flow_statement_response import (
    CodatPublicApiModelsDataCashFlowStatementResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    *,
    client: AuthenticatedClient,
    period_length: int,
    periods_to_compare: int,
    start_month: Union[Unset, None, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    url = "{}/companies/{companyId}/data/financials/cashFlowStatement".format(client.base_url, companyId=company_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["periodLength"] = period_length

    params["periodsToCompare"] = periods_to_compare

    json_start_month: Union[Unset, None, str] = UNSET
    if not isinstance(start_month, Unset):
        json_start_month = start_month.isoformat() if start_month else None

    params["startMonth"] = json_start_month

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
) -> Optional[CodatPublicApiModelsDataCashFlowStatementResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatPublicApiModelsDataCashFlowStatementResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[CodatPublicApiModelsDataCashFlowStatementResponse]:
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
    period_length: int,
    periods_to_compare: int,
    start_month: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[CodatPublicApiModelsDataCashFlowStatementResponse]:
    """Gets the latest cash flow statement for a company.

    Args:
        company_id (str):
        period_length (int):
        periods_to_compare (int):
        start_month (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsDataCashFlowStatementResponse]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        client=client,
        period_length=period_length,
        periods_to_compare=periods_to_compare,
        start_month=start_month,
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
    period_length: int,
    periods_to_compare: int,
    start_month: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[CodatPublicApiModelsDataCashFlowStatementResponse]:
    """Gets the latest cash flow statement for a company.

    Args:
        company_id (str):
        period_length (int):
        periods_to_compare (int):
        start_month (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsDataCashFlowStatementResponse]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        period_length=period_length,
        periods_to_compare=periods_to_compare,
        start_month=start_month,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    period_length: int,
    periods_to_compare: int,
    start_month: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[CodatPublicApiModelsDataCashFlowStatementResponse]:
    """Gets the latest cash flow statement for a company.

    Args:
        company_id (str):
        period_length (int):
        periods_to_compare (int):
        start_month (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsDataCashFlowStatementResponse]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        client=client,
        period_length=period_length,
        periods_to_compare=periods_to_compare,
        start_month=start_month,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: AuthenticatedClient,
    period_length: int,
    periods_to_compare: int,
    start_month: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[CodatPublicApiModelsDataCashFlowStatementResponse]:
    """Gets the latest cash flow statement for a company.

    Args:
        company_id (str):
        period_length (int):
        periods_to_compare (int):
        start_month (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsDataCashFlowStatementResponse]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            period_length=period_length,
            periods_to_compare=periods_to_compare,
            start_month=start_month,
        )
    ).parsed
