from datetime import datetime
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field, HttpUrl


class AgreementRequest(CamelCaseModel):
    pass


class AgreementResponse(CamelCaseModel):
    terms_of_service_url: HttpUrl = Field(
        ...,
        title="Terms of service URL",
        description="URL to the terms of service contents.",
        example="https://example.com/terms-of-service-v1.0",
    )
    description: str = Field(
        ...,
        title="Description",
        description="Description of the terms of service",
        example="This is the terms of service for the example service.",
    )
    version: str = Field(
        ...,
        title="Version",
        description="Version of the terms of service.",
        example="1.0",
    )
    accepted: bool = Field(
        ...,
        title="Accepted",
        description="Whether the service user has accepted the terms of service.",
        example=False,
    )
    accepted_at: Optional[datetime] = Field(
        None,
        title="Accepted at",
        description="When the terms of service was accepted in RFC3339 date-time format. If the service user has not accepted the terms of service, this field is null.",
        example="2023-09-13T11:52:00Z",
        nullable=True,
    )
    accepted_previous_version: bool = Field(
        ...,
        title="Accepted previous version",
        description="Whether the service user has accepted the previous version of the terms of service.",
        example=False,
    )


DEFINITION = DataProductDefinition(
    title="Terms of Service Agreement",
    description="The current terms of service and the service user's agreement to them.",
    request=AgreementRequest,
    response=AgreementResponse,
    requires_authorization=True,
)
