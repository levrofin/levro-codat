import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_public_api_models_data_balance_sheet_response import CodatPublicApiModelsDataBalanceSheetResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    *,
    period_length: int,
    periods_to_compare: int,
    start_month: Union[Unset, None, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    pass

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
        "url": "/companies/{companyId}/data/financials/balanceSheet".format(
            companyId=company_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatPublicApiModelsDataBalanceSheetResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatPublicApiModelsDataBalanceSheetResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatPublicApiModelsDataBalanceSheetResponse]:
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
) -> Response[CodatPublicApiModelsDataBalanceSheetResponse]:
    """Gets the latest balance sheet for a company.

    Args:
        company_id (str):
        period_length (int):
        periods_to_compare (int):
        start_month (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsDataBalanceSheetResponse]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        period_length=period_length,
        periods_to_compare=periods_to_compare,
        start_month=start_month,
    )

    response = client.get_httpx_client().request(
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
) -> Optional[CodatPublicApiModelsDataBalanceSheetResponse]:
    """Gets the latest balance sheet for a company.

    Args:
        company_id (str):
        period_length (int):
        periods_to_compare (int):
        start_month (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatPublicApiModelsDataBalanceSheetResponse
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
) -> Response[CodatPublicApiModelsDataBalanceSheetResponse]:
    """Gets the latest balance sheet for a company.

    Args:
        company_id (str):
        period_length (int):
        periods_to_compare (int):
        start_month (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsDataBalanceSheetResponse]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        period_length=period_length,
        periods_to_compare=periods_to_compare,
        start_month=start_month,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: AuthenticatedClient,
    period_length: int,
    periods_to_compare: int,
    start_month: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[CodatPublicApiModelsDataBalanceSheetResponse]:
    """Gets the latest balance sheet for a company.

    Args:
        company_id (str):
        period_length (int):
        periods_to_compare (int):
        start_month (Union[Unset, None, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatPublicApiModelsDataBalanceSheetResponse
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
