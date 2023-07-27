from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.system_object_push_operation import SystemObjectPushOperation
from ...types import Response


def _get_kwargs(
    company_id: str,
    push_operation_key: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/companies/{companyId}/push/{pushOperationKey}".format(
            companyId=company_id,
            pushOperationKey=push_operation_key,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SystemObjectPushOperation]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SystemObjectPushOperation.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SystemObjectPushOperation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    push_operation_key: str,
    *,
    client: AuthenticatedClient,
) -> Response[SystemObjectPushOperation]:
    """Gets a single push operation record

    Args:
        company_id (str):
        push_operation_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SystemObjectPushOperation]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        push_operation_key=push_operation_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    push_operation_key: str,
    *,
    client: AuthenticatedClient,
) -> Optional[SystemObjectPushOperation]:
    """Gets a single push operation record

    Args:
        company_id (str):
        push_operation_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SystemObjectPushOperation
    """

    return sync_detailed(
        company_id=company_id,
        push_operation_key=push_operation_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    push_operation_key: str,
    *,
    client: AuthenticatedClient,
) -> Response[SystemObjectPushOperation]:
    """Gets a single push operation record

    Args:
        company_id (str):
        push_operation_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SystemObjectPushOperation]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        push_operation_key=push_operation_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    push_operation_key: str,
    *,
    client: AuthenticatedClient,
) -> Optional[SystemObjectPushOperation]:
    """Gets a single push operation record

    Args:
        company_id (str):
        push_operation_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SystemObjectPushOperation
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            push_operation_key=push_operation_key,
            client=client,
        )
    ).parsed
