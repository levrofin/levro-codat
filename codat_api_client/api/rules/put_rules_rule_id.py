from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_public_api_models_rules_rule import CodatPublicApiModelsRulesRule
from ...types import Response


def _get_kwargs(
    rule_id: str,
    *,
    json_body: CodatPublicApiModelsRulesRule,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/rules/{ruleId}".format(
            ruleId=rule_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatPublicApiModelsRulesRule]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatPublicApiModelsRulesRule.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatPublicApiModelsRulesRule]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rule_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsRulesRule,
) -> Response[CodatPublicApiModelsRulesRule]:
    """
    Args:
        rule_id (str):
        json_body (CodatPublicApiModelsRulesRule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsRulesRule]
    """

    kwargs = _get_kwargs(
        rule_id=rule_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    rule_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsRulesRule,
) -> Optional[CodatPublicApiModelsRulesRule]:
    """
    Args:
        rule_id (str):
        json_body (CodatPublicApiModelsRulesRule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatPublicApiModelsRulesRule
    """

    return sync_detailed(
        rule_id=rule_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    rule_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsRulesRule,
) -> Response[CodatPublicApiModelsRulesRule]:
    """
    Args:
        rule_id (str):
        json_body (CodatPublicApiModelsRulesRule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsRulesRule]
    """

    kwargs = _get_kwargs(
        rule_id=rule_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    rule_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsRulesRule,
) -> Optional[CodatPublicApiModelsRulesRule]:
    """
    Args:
        rule_id (str):
        json_body (CodatPublicApiModelsRulesRule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatPublicApiModelsRulesRule
    """

    return (
        await asyncio_detailed(
            rule_id=rule_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
