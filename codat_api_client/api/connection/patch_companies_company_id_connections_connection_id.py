from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_public_api_models_company_data_connection import CodatPublicApiModelsCompanyDataConnection
from ...models.patch_companies_company_id_connections_connection_id_json_body import (
    PatchCompaniesCompanyIdConnectionsConnectionIdJsonBody,
)
from ...types import Response


def _get_kwargs(
    company_id: str,
    connection_id: str,
    *,
    json_body: PatchCompaniesCompanyIdConnectionsConnectionIdJsonBody,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": "/companies/{companyId}/connections/{connectionId}".format(
            companyId=company_id,
            connectionId=connection_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatPublicApiModelsCompanyDataConnection]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatPublicApiModelsCompanyDataConnection.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatPublicApiModelsCompanyDataConnection]:
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
    json_body: PatchCompaniesCompanyIdConnectionsConnectionIdJsonBody,
) -> Response[CodatPublicApiModelsCompanyDataConnection]:
    r"""Disconnect a data source from a company

     This revokes a company’s access to a data source, but the data connection is still listed as a part
    of a company's
    data connection(s). The status value in the request body should be \"Unlinked\" (case sensitive).
    Data connections
    can only be unlinked if in the Linked or Deauthorized state.

    Args:
        company_id (str):
        connection_id (str):
        json_body (PatchCompaniesCompanyIdConnectionsConnectionIdJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsCompanyDataConnection]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        json_body=json_body,
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
    json_body: PatchCompaniesCompanyIdConnectionsConnectionIdJsonBody,
) -> Optional[CodatPublicApiModelsCompanyDataConnection]:
    r"""Disconnect a data source from a company

     This revokes a company’s access to a data source, but the data connection is still listed as a part
    of a company's
    data connection(s). The status value in the request body should be \"Unlinked\" (case sensitive).
    Data connections
    can only be unlinked if in the Linked or Deauthorized state.

    Args:
        company_id (str):
        connection_id (str):
        json_body (PatchCompaniesCompanyIdConnectionsConnectionIdJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatPublicApiModelsCompanyDataConnection
    """

    return sync_detailed(
        company_id=company_id,
        connection_id=connection_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
    json_body: PatchCompaniesCompanyIdConnectionsConnectionIdJsonBody,
) -> Response[CodatPublicApiModelsCompanyDataConnection]:
    r"""Disconnect a data source from a company

     This revokes a company’s access to a data source, but the data connection is still listed as a part
    of a company's
    data connection(s). The status value in the request body should be \"Unlinked\" (case sensitive).
    Data connections
    can only be unlinked if in the Linked or Deauthorized state.

    Args:
        company_id (str):
        connection_id (str):
        json_body (PatchCompaniesCompanyIdConnectionsConnectionIdJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsCompanyDataConnection]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        connection_id=connection_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    connection_id: str,
    *,
    client: AuthenticatedClient,
    json_body: PatchCompaniesCompanyIdConnectionsConnectionIdJsonBody,
) -> Optional[CodatPublicApiModelsCompanyDataConnection]:
    r"""Disconnect a data source from a company

     This revokes a company’s access to a data source, but the data connection is still listed as a part
    of a company's
    data connection(s). The status value in the request body should be \"Unlinked\" (case sensitive).
    Data connections
    can only be unlinked if in the Linked or Deauthorized state.

    Args:
        company_id (str):
        connection_id (str):
        json_body (PatchCompaniesCompanyIdConnectionsConnectionIdJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatPublicApiModelsCompanyDataConnection
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            connection_id=connection_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
