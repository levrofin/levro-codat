from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_public_api_models_rules_add_rule_model import CodatPublicApiModelsRulesAddRuleModel
from ...models.codat_public_api_models_rules_rule import CodatPublicApiModelsRulesRule
from ...types import Response


def _get_kwargs(
    *,
    json_body: CodatPublicApiModelsRulesAddRuleModel,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/rules",
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
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsRulesAddRuleModel,
) -> Response[CodatPublicApiModelsRulesRule]:
    """Subscribe to a rule

    Args:
        json_body (CodatPublicApiModelsRulesAddRuleModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsRulesRule]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsRulesAddRuleModel,
) -> Optional[CodatPublicApiModelsRulesRule]:
    """Subscribe to a rule

    Args:
        json_body (CodatPublicApiModelsRulesAddRuleModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatPublicApiModelsRulesRule
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsRulesAddRuleModel,
) -> Response[CodatPublicApiModelsRulesRule]:
    """Subscribe to a rule

    Args:
        json_body (CodatPublicApiModelsRulesAddRuleModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsRulesRule]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsRulesAddRuleModel,
) -> Optional[CodatPublicApiModelsRulesRule]:
    """Subscribe to a rule

    Args:
        json_body (CodatPublicApiModelsRulesAddRuleModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatPublicApiModelsRulesRule
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
