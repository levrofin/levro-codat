from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_public_api_models_rules_alert_model import CodatPublicApiModelsRulesAlertModel
from ...types import Response


def _get_kwargs(
    alert_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/rules/alerts/{alertId}".format(client.base_url, alertId=alert_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[CodatPublicApiModelsRulesAlertModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatPublicApiModelsRulesAlertModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[CodatPublicApiModelsRulesAlertModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    alert_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatPublicApiModelsRulesAlertModel]:
    """
    Args:
        alert_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsRulesAlertModel]
    """

    kwargs = _get_kwargs(
        alert_id=alert_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alert_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatPublicApiModelsRulesAlertModel]:
    """
    Args:
        alert_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsRulesAlertModel]
    """

    return sync_detailed(
        alert_id=alert_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    alert_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatPublicApiModelsRulesAlertModel]:
    """
    Args:
        alert_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsRulesAlertModel]
    """

    kwargs = _get_kwargs(
        alert_id=alert_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alert_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatPublicApiModelsRulesAlertModel]:
    """
    Args:
        alert_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsRulesAlertModel]
    """

    return (
        await asyncio_detailed(
            alert_id=alert_id,
            client=client,
        )
    ).parsed
