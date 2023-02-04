from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_public_api_models_assess_assess_excel_meta import CodatPublicApiModelsAssessAssessExcelMeta
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    *,
    client: AuthenticatedClient,
    report_type: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/data/companies/{companyId}/assess/excel".format(client.base_url, companyId=company_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["reportType"] = report_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[CodatPublicApiModelsAssessAssessExcelMeta]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatPublicApiModelsAssessAssessExcelMeta.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[CodatPublicApiModelsAssessAssessExcelMeta]:
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
    report_type: Union[Unset, None, str] = UNSET,
) -> Response[CodatPublicApiModelsAssessAssessExcelMeta]:
    """Request an Excel report for download.

    Args:
        company_id (str):
        report_type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsAssessAssessExcelMeta]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        client=client,
        report_type=report_type,
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
    report_type: Union[Unset, None, str] = UNSET,
) -> Optional[CodatPublicApiModelsAssessAssessExcelMeta]:
    """Request an Excel report for download.

    Args:
        company_id (str):
        report_type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsAssessAssessExcelMeta]
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        report_type=report_type,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    report_type: Union[Unset, None, str] = UNSET,
) -> Response[CodatPublicApiModelsAssessAssessExcelMeta]:
    """Request an Excel report for download.

    Args:
        company_id (str):
        report_type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsAssessAssessExcelMeta]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        client=client,
        report_type=report_type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: AuthenticatedClient,
    report_type: Union[Unset, None, str] = UNSET,
) -> Optional[CodatPublicApiModelsAssessAssessExcelMeta]:
    """Request an Excel report for download.

    Args:
        company_id (str):
        report_type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsAssessAssessExcelMeta]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            report_type=report_type,
        )
    ).parsed
