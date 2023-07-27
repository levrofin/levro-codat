from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_public_api_models_company_company import CodatPublicApiModelsCompanyCompany
from ...models.codat_public_api_models_company_update_company_model import CodatPublicApiModelsCompanyUpdateCompanyModel
from ...types import Response


def _get_kwargs(
    company_id: str,
    *,
    json_body: CodatPublicApiModelsCompanyUpdateCompanyModel,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/companies/{companyId}".format(
            companyId=company_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatPublicApiModelsCompanyCompany]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatPublicApiModelsCompanyCompany.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatPublicApiModelsCompanyCompany]:
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
    json_body: CodatPublicApiModelsCompanyUpdateCompanyModel,
) -> Response[CodatPublicApiModelsCompanyCompany]:
    """Update a company with a new name and optional description

    Args:
        company_id (str):
        json_body (CodatPublicApiModelsCompanyUpdateCompanyModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsCompanyCompany]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsCompanyUpdateCompanyModel,
) -> Optional[CodatPublicApiModelsCompanyCompany]:
    """Update a company with a new name and optional description

    Args:
        company_id (str):
        json_body (CodatPublicApiModelsCompanyUpdateCompanyModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatPublicApiModelsCompanyCompany
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsCompanyUpdateCompanyModel,
) -> Response[CodatPublicApiModelsCompanyCompany]:
    """Update a company with a new name and optional description

    Args:
        company_id (str):
        json_body (CodatPublicApiModelsCompanyUpdateCompanyModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsCompanyCompany]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: AuthenticatedClient,
    json_body: CodatPublicApiModelsCompanyUpdateCompanyModel,
) -> Optional[CodatPublicApiModelsCompanyCompany]:
    """Update a company with a new name and optional description

    Args:
        company_id (str):
        json_body (CodatPublicApiModelsCompanyUpdateCompanyModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatPublicApiModelsCompanyCompany
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
