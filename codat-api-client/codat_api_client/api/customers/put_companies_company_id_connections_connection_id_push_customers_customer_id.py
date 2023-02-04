from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_data_contracts_datasets_customer import CodatDataContractsDatasetsCustomer
from ...models.codat_data_contracts_datasets_customer_push_operation import (
    CodatDataContractsDatasetsCustomerPushOperation,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    company_id: str,
    connection_id: str,
    customer_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatDataContractsDatasetsCustomer,
    timeout_in_minutes: Union[Unset, None, int] = UNSET,
    force_update: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/companies/{companyId}/connections/{connectionId}/push/customers/{customerId}".format(
        client.base_url, companyId=company_id, connectionId=connection_id, customerId=customer_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["timeoutInMinutes"] = timeout_in_minutes

    params["forceUpdate"] = force_update

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[CodatDataContractsDatasetsCustomerPushOperation]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatDataContractsDatasetsCustomerPushOperation.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[CodatDataContractsDatasetsCustomerPushOperation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    connection_id: str,
    customer_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatDataContractsDatasetsCustomer,
    timeout_in_minutes: Union[Unset, None, int] = UNSET,
    force_update: Union[Unset, None, bool] = False,
) -> Response[CodatDataContractsDatasetsCustomerPushOperation]:
    """Posts an updated customer for a given company.

    Args:
        company_id (str):
        connection_id (str):
        customer_id (str):
        timeout_in_minutes (Union[Unset, None, int]):
        force_update (Union[Unset, None, bool]):
        json_body (CodatDataContractsDatasetsCustomer):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsCustomerPushOperation]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        customer_id=customer_id,
        client=client,
        json_body=json_body,
        timeout_in_minutes=timeout_in_minutes,
        force_update=force_update,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    connection_id: str,
    customer_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatDataContractsDatasetsCustomer,
    timeout_in_minutes: Union[Unset, None, int] = UNSET,
    force_update: Union[Unset, None, bool] = False,
) -> Optional[CodatDataContractsDatasetsCustomerPushOperation]:
    """Posts an updated customer for a given company.

    Args:
        company_id (str):
        connection_id (str):
        customer_id (str):
        timeout_in_minutes (Union[Unset, None, int]):
        force_update (Union[Unset, None, bool]):
        json_body (CodatDataContractsDatasetsCustomer):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsCustomerPushOperation]
    """

    return sync_detailed(
        company_id=company_id,
        connection_id=connection_id,
        customer_id=customer_id,
        client=client,
        json_body=json_body,
        timeout_in_minutes=timeout_in_minutes,
        force_update=force_update,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    connection_id: str,
    customer_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatDataContractsDatasetsCustomer,
    timeout_in_minutes: Union[Unset, None, int] = UNSET,
    force_update: Union[Unset, None, bool] = False,
) -> Response[CodatDataContractsDatasetsCustomerPushOperation]:
    """Posts an updated customer for a given company.

    Args:
        company_id (str):
        connection_id (str):
        customer_id (str):
        timeout_in_minutes (Union[Unset, None, int]):
        force_update (Union[Unset, None, bool]):
        json_body (CodatDataContractsDatasetsCustomer):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsCustomerPushOperation]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        customer_id=customer_id,
        client=client,
        json_body=json_body,
        timeout_in_minutes=timeout_in_minutes,
        force_update=force_update,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    connection_id: str,
    customer_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatDataContractsDatasetsCustomer,
    timeout_in_minutes: Union[Unset, None, int] = UNSET,
    force_update: Union[Unset, None, bool] = False,
) -> Optional[CodatDataContractsDatasetsCustomerPushOperation]:
    """Posts an updated customer for a given company.

    Args:
        company_id (str):
        connection_id (str):
        customer_id (str):
        timeout_in_minutes (Union[Unset, None, int]):
        force_update (Union[Unset, None, bool]):
        json_body (CodatDataContractsDatasetsCustomer):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatDataContractsDatasetsCustomerPushOperation]
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            connection_id=connection_id,
            customer_id=customer_id,
            client=client,
            json_body=json_body,
            timeout_in_minutes=timeout_in_minutes,
            force_update=force_update,
        )
    ).parsed
