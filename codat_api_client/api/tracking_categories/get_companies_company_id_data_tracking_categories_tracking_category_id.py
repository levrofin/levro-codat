from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.codat_public_api_models_data_tracking_category_tree import CodatPublicApiModelsDataTrackingCategoryTree
from ...types import Response


def _get_kwargs(
    company_id: str,
    tracking_category_id: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/companies/{companyId}/data/trackingCategories/{trackingCategoryId}".format(
            companyId=company_id,
            trackingCategoryId=tracking_category_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CodatPublicApiModelsDataTrackingCategoryTree]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CodatPublicApiModelsDataTrackingCategoryTree.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CodatPublicApiModelsDataTrackingCategoryTree]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    tracking_category_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatPublicApiModelsDataTrackingCategoryTree]:
    """Gets the specified tracking categories for a given company.

    Args:
        company_id (str):
        tracking_category_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsDataTrackingCategoryTree]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        tracking_category_id=tracking_category_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    tracking_category_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatPublicApiModelsDataTrackingCategoryTree]:
    """Gets the specified tracking categories for a given company.

    Args:
        company_id (str):
        tracking_category_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatPublicApiModelsDataTrackingCategoryTree
    """

    return sync_detailed(
        company_id=company_id,
        tracking_category_id=tracking_category_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    tracking_category_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CodatPublicApiModelsDataTrackingCategoryTree]:
    """Gets the specified tracking categories for a given company.

    Args:
        company_id (str):
        tracking_category_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CodatPublicApiModelsDataTrackingCategoryTree]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
        tracking_category_id=tracking_category_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    tracking_category_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[CodatPublicApiModelsDataTrackingCategoryTree]:
    """Gets the specified tracking categories for a given company.

    Args:
        company_id (str):
        tracking_category_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CodatPublicApiModelsDataTrackingCategoryTree
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            tracking_category_id=tracking_category_id,
            client=client,
        )
    ).parsed
